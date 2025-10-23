"""
Browser Automation with MCP + Playwright + Gemini LLM
Natural language browser control - you can see the browser in action!

Usage:
    python browser_automation.py "your instruction here"
    
Examples:
    python browser_automation.py "Open https://www.google.com"
    python browser_automation.py "Go to GitHub and search for python projects"
    python browser_automation.py "Navigate to Wikipedia and search for artificial intelligence"
"""

import os
import json
import asyncio
import platform
import shutil
import sys
from typing import Any, Dict
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Gemini SDK
from google import genai
from google.genai import types as gtypes

# MCP SDK
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

# Configuration
MODEL = "gemini-2.0-flash-exp"  # Fast and capable Gemini model
HEADLESS = False  # Set to True to hide the browser window


def _npx_command() -> str:
    """Resolve npx launcher cross-platform; prefer npx.cmd on Windows."""
    if platform.system().lower().startswith("win"):
        return shutil.which("npx.cmd") or "npx.cmd"
    return shutil.which("npx") or "npx"


def clean_schema(obj):
    """Recursively clean MCP schemas to be compatible with Gemini."""
    if isinstance(obj, dict):
        cleaned = {}
        for k, v in obj.items():
            # Skip problematic keys that Gemini doesn't support
            if k in ("$schema", "additionalProperties", "$id", "$defs", "definitions", "$ref", "examples"):
                continue
            cleaned[k] = clean_schema(v)
        return cleaned
    elif isinstance(obj, list):
        return [clean_schema(item) for item in obj]
    else:
        return obj


async def run_browser_automation(user_instruction: str):
    """Execute a browser automation task based on natural language instruction."""
    
    # Start Playwright MCP via stdio with headed mode
    npx = _npx_command()
    print(f"[INFO] Using npx launcher: {npx}")
    print(f"[INFO] Browser mode: {'HEADLESS' if HEADLESS else 'HEADED (visible)'}")

    # Configure environment for Playwright - set headless mode
    env = os.environ.copy()
    if not HEADLESS:
        # Force headed mode by not setting PLAYWRIGHT_HEADLESS
        env.pop('PLAYWRIGHT_HEADLESS', None)
    
    # Configure Playwright MCP server
    server = StdioServerParameters(
        command=npx,
        args=["@playwright/mcp@latest"],
        env=env,
    )

    async with stdio_client(server) as (read, write):
        async with ClientSession(read, write) as session:
            print("[INFO] Initializing MCP session...")
            await session.initialize()
            
            print("[INFO] Connected to Playwright MCP server")
            print("[INFO] Listing available browser tools...")
            tools_resp = await session.list_tools()
            mcp_tools = tools_resp.tools
            print(f"[INFO] Found {len(mcp_tools)} browser automation tools")

            # Convert MCP tool schemas → Gemini function declarations
            gemini_fns = []
            for tool in mcp_tools:
                schema = tool.inputSchema or {"type": "object", "properties": {}}
                clean = clean_schema(schema)
                
                gemini_fns.append(gtypes.FunctionDeclaration(
                    name=tool.name,
                    description=tool.description or "",
                    parameters=clean,
                ))

            # Get Gemini API key
            api_key = os.environ.get("GEMINI_API_KEY")
            if not api_key:
                raise RuntimeError("GEMINI_API_KEY is not set in .env file")

            client = genai.Client(api_key=api_key)

            # System instructions for the AI agent
            system_instructions = (
                "You are a browser automation agent with access to Playwright browser tools. "
                "Use browser_navigate to open URLs. "
                "Use browser_snapshot to view page content. "
                "Use browser_click to click elements. "
                "Use browser_type to enter text. "
                "Use browser_screenshot to capture images. "
                "Always provide a friendly summary of what you did."
            )

            print(f"\n{'='*60}")
            print(f"USER INSTRUCTION: {user_instruction}")
            print(f"{'='*60}\n")
            
            print("[INFO] Asking Gemini to plan the browser actions...")
            
            # Ask Gemini to decide what to do
            response = client.models.generate_content(
                model=MODEL,
                contents=[
                    gtypes.Content(
                        role="user",
                        parts=[gtypes.Part(text=f"{system_instructions}\n\nUser request: {user_instruction}")]
                    )
                ],
                config=gtypes.GenerateContentConfig(
                    tools=[gtypes.Tool(function_declarations=gemini_fns)],
                    tool_config=gtypes.ToolConfig(
                        function_calling_config=gtypes.FunctionCallingConfig(mode="AUTO")
                    ),
                ),
            )

            if not response.candidates:
                print("[ERROR] No response from Gemini AI")
                return

            # Multi-step execution loop - allow multiple tool calls
            conversation_history = [
                gtypes.Content(
                    role="user",
                    parts=[gtypes.Part(text=f"{system_instructions}\n\nUser request: {user_instruction}")]
                )
            ]
            
            max_steps = 50  # Maximum number of tool calls to prevent infinite loops
            step_count = 0
            
            while step_count < max_steps:
                parts = response.candidates[0].content.parts
                
                # Check if Gemini wants to call a browser tool
                function_call = next(
                    (p.function_call for p in parts if hasattr(p, "function_call") and p.function_call), 
                    None
                )
                
                if not function_call:
                    # No tool call, just text response - we're done
                    text = next((p.text for p in parts if hasattr(p, "text")), "")
                    if text:
                        print(f"\n{'='*60}")
                        print("FINAL AI RESPONSE:")
                        print(f"{'='*60}")
                        print(text)
                        print(f"{'='*60}\n")
                    else:
                        print(f"\n[INFO] Task completed after {step_count} steps\n")
                    break

                step_count += 1
                
                # Execute the browser tool
                tool_name = function_call.name
                tool_args = function_call.args if hasattr(function_call, 'args') and function_call.args else {}
                
                print(f"\n{'='*60}")
                print(f"STEP {step_count}: {tool_name}")
                print(f"{'='*60}")
                print(f"[ARGUMENTS] {json.dumps(tool_args, indent=2, default=str)}\n")

                try:
                    # Execute the tool via MCP
                    result = await session.call_tool(tool_name, arguments=tool_args)
                    print(f"[SUCCESS] Tool '{tool_name}' executed successfully")
                    
                    # Extract result text
                    result_text = ""
                    if result.content:
                        for content_item in result.content:
                            if hasattr(content_item, "text"):
                                result_text += content_item.text + "\n"
                    
                    # Show abbreviated result
                    if len(result_text) > 500:
                        print(f"[RESULT] {result_text[:500]}... (truncated)")
                    else:
                        print(f"[RESULT] {result_text}")
                    
                    # Add model's response and tool result to conversation
                    conversation_history.append(gtypes.Content(role="model", parts=parts))
                    conversation_history.append(
                        gtypes.Content(
                            role="user", 
                            parts=[gtypes.Part(text=f"Tool result:\n{result_text}\n\nContinue with the next step or provide a final summary if done.")]
                        )
                    )
                    
                    # Ask Gemini for next step
                    response = client.models.generate_content(
                        model=MODEL,
                        contents=conversation_history,
                        config=gtypes.GenerateContentConfig(
                            tools=[gtypes.Tool(function_declarations=gemini_fns)],
                            tool_config=gtypes.ToolConfig(
                                function_calling_config=gtypes.FunctionCallingConfig(mode="AUTO")
                            ),
                        ),
                    )
                    
                except Exception as e:
                    print(f"\n[ERROR] Tool execution failed: {e}")
                    # Try to continue with error feedback
                    conversation_history.append(gtypes.Content(role="model", parts=parts))
                    conversation_history.append(
                        gtypes.Content(
                            role="user", 
                            parts=[gtypes.Part(text=f"Error occurred: {e}\n\nTry a different approach or provide a summary.")]
                        )
                    )
                    response = client.models.generate_content(
                        model=MODEL,
                        contents=conversation_history,
                        config=gtypes.GenerateContentConfig(
                            tools=[gtypes.Tool(function_declarations=gemini_fns)],
                            tool_config=gtypes.ToolConfig(
                                function_calling_config=gtypes.FunctionCallingConfig(mode="AUTO")
                            ),
                        ),
                    )
            
            if step_count >= max_steps:
                print(f"\n[WARNING] Reached maximum step limit ({max_steps}). Stopping.")


def main():
    """Main entry point."""
    print("\n" + "="*60)
    print("Browser Automation with MCP + Playwright + Gemini")
    print("="*60 + "\n")
    
    if len(sys.argv) > 1:
        # Use command line argument if provided
        instruction = " ".join(sys.argv[1:])
    else:
        # Interactive mode - ask for instruction
        print("No instruction provided. Enter your browser automation task:")
        print("\nExamples:")
        print('  - "Open https://www.google.com"')
        print('  - "Go to GitHub and take a screenshot"')
        print('  - "Navigate to Wikipedia and search for Python"')
        print()
        instruction = input("Your instruction: ").strip()
        
        if not instruction:
            print("\n[ERROR] No instruction provided. Exiting.")
            return
    
    try:
        asyncio.run(run_browser_automation(instruction))
    except KeyboardInterrupt:
        print("\n\n[INFO] Interrupted by user. Exiting...")
    except Exception as e:
        print(f"\n[FATAL ERROR] {e}\n")
        import traceback
        traceback.print_exc()


if __name__ == "__main__":
    main()
