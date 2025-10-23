# Quick Start Guide

## Single Command to Run

```powershell
python browser_automation.py "your instruction here"
```

## Examples

```powershell
# Open Google
python browser_automation.py "Open https://www.google.com"

# Visit GitHub
python browser_automation.py "Go to GitHub"

# Take a screenshot
python browser_automation.py "Navigate to Wikipedia and take a screenshot"

# Interactive search (more complex)
python browser_automation.py "Go to Google and search for Python tutorials"
```

## Interactive Mode

Just run without arguments:
```powershell
python browser_automation.py
```

Then enter your instruction when prompted.

## Browser Visibility

**The browser window is VISIBLE by default** so you can watch the automation!

To hide it, edit `browser_automation.py` line 36:
```python
HEADLESS = True  # Change False to True
```

## What You Can Ask It To Do

- Navigate to websites
- View page content
- Take screenshots
- Click on elements
- Type text
- Wait for page loads
- And much more!

## Files You Need

✅ `browser_automation.py` - The main script (this is all you need!)
✅ `.env` - Your Gemini API key
✅ `requirements.txt` - Dependencies list

That's it! Enjoy automated browsing! 🚀
