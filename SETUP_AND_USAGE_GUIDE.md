# Complete Setup and Usage Guide
## Browser Automation with MCP + Playwright + Gemini

---

## 📋 Table of Contents
1. [Setup Instructions](#setup-instructions)
2. [Basic Usage](#basic-usage)
3. [Simple Examples](#simple-examples)
4. [Complex Interactions](#complex-interactions)
5. [Advanced Multi-Step Scenarios](#advanced-multi-step-scenarios)
6. [Troubleshooting](#troubleshooting)

---

## 🚀 Setup Instructions

### Prerequisites
- ✅ Python 3.11 or higher
- ✅ Node.js (for npx and Playwright MCP)
- ✅ Git (optional, for cloning)
- ✅ Gemini API key (free tier available)

### Step 1: Install Python Dependencies
```powershell
# Navigate to project directory
cd "c:\Users\user\Desktop\projects\playwrgiht mcp"

# Install required packages
pip install google-genai mcp python-dotenv
```

### Step 2: Configure API Key
Your `.env` file should contain:
```
GEMINI_API_KEY=your_api_key_here
```

The current setup already has this configured.

### Step 3: Verify Installation
```powershell
# Test with a simple command
python browser_automation.py "Open https://www.google.com"
```

If a browser window opens and navigates to Google, you're all set! ✅

---

## 💡 Basic Usage

### Command Line Mode (Recommended)
```powershell
python browser_automation.py "your instruction here"
```

### Interactive Mode
```powershell
python browser_automation.py
# Then enter your instruction when prompted
```

### Browser Visibility
- **Default**: Browser window is VISIBLE (headed mode)
- **To hide**: Edit line 36 in `browser_automation.py` and set `HEADLESS = True`

---

## 🎯 Simple Examples

### Navigation
```powershell
# Open a website
python browser_automation.py "Open https://www.google.com"

# Navigate to GitHub
python browser_automation.py "Go to https://github.com"

# Visit multiple sites
python browser_automation.py "Open Google, then go to Wikipedia, then visit YouTube"
```

### Screenshots
```powershell
# Take a screenshot
python browser_automation.py "Go to Google and take a screenshot"

# Multiple screenshots
python browser_automation.py "Visit GitHub and save screenshot as github.png, then go to Stack Overflow and save screenshot as stackoverflow.png"
```

### Page Content
```powershell
# View page content
python browser_automation.py "Open Wikipedia and show me the page content"

# Get specific information
python browser_automation.py "Go to Hacker News and tell me the first post title"
```

---

## 🎨 Complex Interactions

### 1. Clicking Buttons

#### Simple Button Click
```powershell
python browser_automation.py "Go to Google, click the 'I'm Feeling Lucky' button"
```

#### Click Specific Elements
```powershell
# Click navigation links
python browser_automation.py "Open GitHub, click the 'Pricing' link in the navigation"

# Click search button
python browser_automation.py "Go to Wikipedia, type 'Python programming' in the search box, then click the Search button"
```

#### Multiple Clicks in Sequence
```powershell
python browser_automation.py "Open Hacker News, click the 'new' link, wait 2 seconds, then click the first story link"
```

### 2. Filling Input Fields

#### Simple Text Input
```powershell
python browser_automation.py "Go to Google, type 'machine learning tutorials' in the search box"
```

#### Form Filling
```powershell
python browser_automation.py "Open a contact form, type 'John Doe' in the name field, type 'john@example.com' in the email field, type 'Hello' in the message field"
```

#### Search and Submit
```powershell
python browser_automation.py "Go to YouTube, search for 'Python tutorials', press Enter"
```

### 3. Dropdown Selection

#### Single Dropdown
```powershell
python browser_automation.py "Open the form, select 'United States' from the country dropdown"
```

#### Multiple Dropdowns
```powershell
python browser_automation.py "Fill the form: select 'Mr.' from title dropdown, select 'United States' from country dropdown, select 'New York' from state dropdown"
```

### 4. Checkbox and Radio Buttons

#### Checkboxes
```powershell
python browser_automation.py "Open the signup form, check the 'I agree to terms' checkbox, check the 'Subscribe to newsletter' checkbox"
```

#### Radio Buttons
```powershell
python browser_automation.py "Fill the survey: select the 'Very Satisfied' radio button for question 1, select 'Recommend' for question 2"
```

### 5. Form Filling (Complete Example)

```powershell
python browser_automation.py "Open the registration form, fill in First Name as 'John', Last Name as 'Doe', Email as 'john@example.com', select 'United States' from country dropdown, check the terms checkbox, then click Submit"
```

### 6. Hover and Mouse Actions

#### Hover to Reveal Menu
```powershell
python browser_automation.py "Go to the website, hover over the 'Products' menu to reveal dropdown options, then click 'Software'"
```

#### Drag and Drop
```powershell
python browser_automation.py "Open the page, drag the blue box to the drop zone on the right"
```

### 7. Tab Management

#### Open New Tab
```powershell
python browser_automation.py "Open Google in the first tab, open a new tab and go to GitHub, then switch back to the first tab"
```

#### Multiple Tabs
```powershell
python browser_automation.py "Open tabs for Google, GitHub, and Stack Overflow, take a screenshot of each, then close all tabs except the first one"
```

### 8. Waiting for Elements

#### Wait for Content
```powershell
python browser_automation.py "Go to the page, wait for the 'Loading...' text to disappear, then click the Continue button"
```

#### Wait with Timeout
```powershell
python browser_automation.py "Open the page, wait 5 seconds for content to load, then take a screenshot"
```

### 9. Complex Navigation

#### Back and Forward
```powershell
python browser_automation.py "Open Google, search for Python, click first result, go back, search for JavaScript, click first result"
```

#### Scroll and Click
```powershell
python browser_automation.py "Go to the page, scroll down to the footer, click the Privacy Policy link"
```

---

## 🏆 Advanced Multi-Step Scenarios

### Scenario 1: E-commerce Shopping Flow
```powershell
python browser_automation.py "Go to the online store, search for 'laptop', select the first product, select '16GB RAM' from the configuration dropdown, select 'Silver' color, set quantity to 2, take a screenshot of the product page, click Add to Cart, go to cart and take a final screenshot"
```

### Scenario 2: Social Media Interaction
```powershell
python browser_automation.py "Open Twitter, search for 'artificial intelligence', click the Latest tab, take a screenshot of the first 5 tweets, click the first tweet to open it, take a screenshot of the full thread"
```

### Scenario 3: Research and Documentation
```powershell
python browser_automation.py "Search Google for 'Python documentation', click the official docs link, navigate to the Tutorial section, take screenshots of the first 3 tutorial pages, go back to Google and search for 'Python examples', click the first GitHub repository link"
```

### Scenario 4: Form Submission Flow
```powershell
python browser_automation.py "Open the registration page, fill Name as 'Jane Smith', Email as 'jane@example.com', select 'Female' from gender dropdown, select 'United States' from country dropdown, type '90210' in zip code, check 'I agree to terms' checkbox, check 'Send me updates' checkbox, click the Submit button, wait for confirmation message, take a screenshot"
```

### Scenario 5: Multi-Site Research
```powershell
python browser_automation.py "Research Python frameworks: Go to Google and search for 'best Python web frameworks', take a screenshot, click the first article, read and summarize the top 3 frameworks, then visit each framework's official website (Django, Flask, FastAPI), take screenshots of their homepages, and provide a summary comparison"
```

### Scenario 6: Price Comparison
```powershell
python browser_automation.py "Compare laptop prices: Search for 'Dell XPS 15' on Amazon, note the price and take a screenshot, then search the same on Best Buy website, note that price and take a screenshot, then search on Newegg, take a screenshot, and provide a price comparison summary"
```

### Scenario 7: Content Aggregation
```powershell
python browser_automation.py "Gather tech news: Visit Hacker News and screenshot the top story, visit TechCrunch and screenshot the featured article, visit The Verge and screenshot the main headline, visit Ars Technica and screenshot their top story, then provide a summary of all headlines"
```

### Scenario 8: Account Creation Flow
```powershell
python browser_automation.py "Create an account: Go to the signup page, fill username as 'testuser123', fill email as 'test@example.com', fill password as 'SecurePass123', confirm password as 'SecurePass123', select '1990' from birth year dropdown, select 'January' from month dropdown, select '15' from day dropdown, select 'United States' from country, check terms agreement, click Create Account, wait for welcome message, take confirmation screenshot"
```

---

## 🔧 Available Browser Tools

The AI agent has access to these Playwright tools:

| Tool | Description | Example Usage |
|------|-------------|---------------|
| `browser_navigate` | Navigate to URL | "Go to Google" |
| `browser_click` | Click element | "Click the Submit button" |
| `browser_type` | Type text | "Type 'hello' in the search box" |
| `browser_screenshot` | Capture image | "Take a screenshot" |
| `browser_snapshot` | Get page content | "Show me the page content" |
| `browser_wait_for` | Wait for condition | "Wait 3 seconds" |
| `browser_tabs` | Manage tabs | "Open a new tab" |
| `browser_press_key` | Keyboard input | "Press Enter" |
| `browser_hover` | Mouse hover | "Hover over the menu" |
| `browser_drag` | Drag and drop | "Drag item to zone" |
| `browser_select_option` | Select dropdown | "Select 'USA' from country" |
| `browser_fill_form` | Fill entire form | "Fill the registration form" |
| `browser_navigate_back` | Go back | "Go back to previous page" |
| `browser_network_requests` | View network | "Show network requests" |
| `browser_file_upload` | Upload files | "Upload document.pdf" |

---

## 🎯 Tips for Complex Instructions

### 1. Be Specific About Elements
✅ Good: "Click the blue 'Submit' button at the bottom"  
❌ Vague: "Click the button"

### 2. Chain Actions Logically
✅ Good: "Type 'hello', wait 1 second, then press Enter"  
❌ Unclear: "Type hello and submit"

### 3. Include Waits for Dynamic Content
✅ Good: "Click search, wait for results to load, then take screenshot"  
❌ Hasty: "Click search and screenshot"

### 4. Use Clear Field Identifiers
✅ Good: "Type 'John' in the First Name field"  
❌ Ambiguous: "Type John"

### 5. Specify Order for Multiple Actions
✅ Good: "First fill name, then email, then click submit"  
❌ Confusing: "Fill name and email and submit"

---

## 🐛 Troubleshooting

### Issue: "API quota exceeded"
**Solution**: Wait 6 seconds and retry, or upgrade to paid Gemini API tier

### Issue: Browser doesn't open
**Solution**: 
- Check Node.js is installed: `node --version`
- Check npx is available: `npx --version`
- Verify Playwright MCP can run: `npx @playwright/mcp@latest`

### Issue: Element not found
**Solution**: 
- Add wait time: "wait 2 seconds before clicking"
- Be more specific about element: "click the red Submit button in the footer"
- Take a screenshot first to see page state

### Issue: Too many steps
**Solution**: 
- Break into smaller tasks
- Script has 50-step limit to prevent infinite loops
- For very long processes, run in batches

### Issue: Rate limiting
**Solution**:
- Free tier has limits: 250,000 tokens per minute
- Add delays between operations
- Consider upgrading API plan

---

## 📊 Performance Tips

### For Faster Execution
- Use specific element selectors
- Minimize screenshots (they're slower)
- Skip unnecessary waits
- Combine multiple actions in one instruction

### For Better Accuracy
- Add wait times for dynamic content
- Take screenshots to verify state
- Use specific element descriptions
- Break complex tasks into smaller steps

---

## 🎓 Learning Path

### Beginner
1. Start with simple navigation
2. Try taking screenshots
3. Practice clicking buttons

### Intermediate
4. Fill forms with text input
5. Work with dropdowns
6. Handle checkboxes and radio buttons

### Advanced
7. Multi-step workflows
8. Tab management
9. Complex form submissions
10. Research and aggregation tasks

---

## 📝 Quick Reference

```powershell
# Navigate
python browser_automation.py "Go to [URL]"

# Click
python browser_automation.py "Click the [element description]"

# Type
python browser_automation.py "Type '[text]' in the [field name]"

# Select dropdown
python browser_automation.py "Select '[option]' from [dropdown name]"

# Screenshot
python browser_automation.py "Take a screenshot"

# Multi-step
python browser_automation.py "Do [action 1], then [action 2], then [action 3]"
```

---

## ✅ You're Ready!

Start with simple commands and gradually build up to complex multi-step automations. The AI agent will handle the technical details and adapt to different website structures.

Happy automating! 🚀

---

## 📚 Additional Resources

- See `30_step_automation.md` for complex scenario examples
- See `QUICKSTART.md` for quick command reference
- See `SUMMARY.md` for feature overview
- Check `.env` file for API configuration
