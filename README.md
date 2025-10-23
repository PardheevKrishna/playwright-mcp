# Browser Automation with MCP + Playwright + Gemini LLM

Control a web browser using natural language instructions - **you can see the browser in action!**

This combines:
- **Playwright MCP Server**: Provides browser automation capabilities
- **Google Gemini AI**: Interprets your instructions and decides which browser actions to take
- **Python MCP Client**: Connects everything together

## Prerequisites

✅ All installed:
- Python 3.11
- Node.js v22.21.0
- npx 10.9.4

## Installation

1. **Install Python dependencies**:
```powershell
pip install google-genai mcp python-dotenv
```

2. **Set up your Gemini API key**:
The `.env` file already contains your API key:
```
GEMINI_API_KEY=AIzaSyBvQQ0N2P_fimDDUPphRQc_Rrmpd5Fo_28
```

3. **The Playwright MCP server** will be automatically downloaded via npx when you run the script.

## Usage

### Interactive Mode

Run without arguments for interactive mode:
```powershell
python browser_automation.py
```

You'll be prompted to enter your instruction.

### Command Line Mode

Pass your instruction as a command-line argument:
```powershell
python browser_automation.py "Open https://news.ycombinator.com and tell me the first story"
```

```powershell
python browser_automation.py "Go to https://github.com and take a screenshot"
```

```powershell
python browser_automation.py "Navigate to https://www.google.com and search for Python tutorials"
```

## Example Instructions

Here are some things you can ask it to do:

- `"Open https://www.google.com"`
- `"Navigate to https://news.ycombinator.com and view the page content"`
- `"Go to https://github.com and take a screenshot"`
- `"Open https://www.wikipedia.org and search for 'artificial intelligence'"`
- `"Navigate to https://www.python.org and tell me the latest Python version"`

## How It Works

1. **You provide** a natural language instruction
2. **Gemini LLM** interprets your instruction and decides which browser automation tool to use
3. **Playwright MCP** executes the browser action (navigate, click, type, screenshot, etc.)
4. **Results** are sent back to Gemini which provides a human-friendly summary

## Available Browser Actions

The Playwright MCP server provides these tools:
- `browser_navigate` - Navigate to a URL
- `browser_snapshot` - Get the current page content
- `browser_click` - Click on elements
- `browser_type` - Type text into fields
- `browser_screenshot` - Take screenshots
- `browser_wait_for` - Wait for elements or conditions
- `browser_tabs` - Manage browser tabs
- And many more!

## Troubleshooting

### DNS Resolution Errors
If you see `ERR_NAME_NOT_RESOLVED`, it means your network can't reach the website. Try:
- Check your internet connection
- Try a different website
- Use an IP address instead of domain name

### Model Overloaded
If you see `503 UNAVAILABLE - model overloaded`, the Gemini model is busy. The script uses `gemini-2.0-flash-exp` which is generally available. You can also try:
- `gemini-1.5-flash`
- `gemini-1.5-pro`

### Schema Errors
The script includes aggressive schema cleanup to handle incompatibilities between MCP and Gemini's function calling formats.

## Browser Display Mode

By default, the browser window is **VISIBLE (headed mode)** so you can watch the automation happen!

To hide the browser window, edit `browser_automation.py` and change:
```python
HEADLESS = False  # Change to True to hide the browser
```

## Files

- `browser_automation.py` - **The only script you need!** Complete browser automation
- `.env` - Contains your Gemini API key
- `requirements.txt` - Python dependencies
- `README.md` - This file

## Next Steps

- Modify the instruction in `main_simple.py` to suit your needs
- Build multi-step automations by extending the code
- Add error handling and retry logic
- Create a loop for interactive conversations

## Credits

- Playwright MCP: https://github.com/microsoft/playwright-mcp
- Google Gemini: https://ai.google.dev/
- MCP (Model Context Protocol): https://modelcontextprotocol.io/
