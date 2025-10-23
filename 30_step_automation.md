# Complex 30-Step Browser Automation Test

## Scenario: Research and Documentation Task

Navigate to Google and perform a comprehensive research task involving multiple websites, capturing screenshots, and gathering information.

## Detailed Steps:

1. Navigate to https://www.google.com
2. Take a screenshot of the Google homepage and save it as 'google-home.png'
3. Search for "GitHub trending repositories"
4. Take a screenshot of the search results
5. Click on the first GitHub link in the results
6. Wait for the GitHub page to load (wait 2 seconds)
7. Take a screenshot of the GitHub trending page
8. Capture the page title
9. Go back to the previous page
10. Navigate to https://news.ycombinator.com
11. Take a screenshot of Hacker News homepage
12. Click on the "new" link
13. Wait for the new page to load
14. Take a screenshot of the new posts page
15. Navigate to https://stackoverflow.com
16. Take a screenshot of Stack Overflow homepage
17. Navigate to https://www.wikipedia.org
18. Take a screenshot of Wikipedia homepage
19. Search for "Artificial Intelligence" in Wikipedia
20. Wait for search results (wait 1 second)
21. Take a screenshot of the search results
22. Click on the first result
23. Wait for the article to load (wait 2 seconds)
24. Take a screenshot of the article
25. Navigate to https://www.reddit.com
26. Take a screenshot of Reddit homepage
27. Navigate to https://www.youtube.com
28. Take a screenshot of YouTube homepage
29. Navigate back to Google (https://www.google.com)
30. Take a final screenshot and provide a summary of all visited sites

---

## How to Execute:

### Option 1: Direct Command
```powershell
python browser_automation.py "Navigate to Google, take a screenshot named google-home.png, then search for GitHub trending repositories, click the first result, take a screenshot, go back, visit Hacker News and take a screenshot of homepage and the new page, then visit Stack Overflow and take a screenshot, then go to Wikipedia and search for Artificial Intelligence and take screenshots of results and the article, then visit Reddit and YouTube taking screenshots of each, finally return to Google and summarize all the sites visited"
```

### Option 2: Load from File
```powershell
# Read the complex instruction from this file
$instruction = Get-Content "30_step_automation.md" -Raw
python browser_automation.py $instruction
```

### Option 3: Simplified Test (Recommended First)
```powershell
python browser_automation.py "Go to Google, take a screenshot, search for GitHub, click the first result, take a screenshot, then go to Wikipedia, search for Python programming, and take a final screenshot"
```

---

## Expected Outcomes:

- Multiple website visits
- Screenshots saved at each step
- Navigation between different sites
- Search functionality tested
- Click interactions performed
- Wait operations executed
- Back navigation tested
- Final summary of all actions

---

## Simplified 10-Step Version (for faster testing):

1. Navigate to https://www.google.com
2. Take a screenshot of Google homepage
3. Search for "GitHub"
4. Click on the first result
5. Take a screenshot of GitHub
6. Navigate to https://www.wikipedia.org
7. Search for "Python programming"
8. Take a screenshot of Wikipedia search results
9. Navigate back to Google
10. Provide a summary of visited sites

### Command for 10-step version:
```powershell
python browser_automation.py "Visit Google and take a screenshot, search for GitHub and click the first result and screenshot it, then go to Wikipedia and search for Python programming and take a screenshot, finally go back to Google and summarize everything"
```

---

## Tips:

- The browser window will be visible (headed mode) so you can watch the automation
- Each screenshot will be saved in the current directory
- The AI will adapt if any step fails
- You can interrupt with Ctrl+C at any time
- Complex multi-step tasks may take several minutes to complete

---

## Note:

The AI agent (Gemini) will interpret these instructions and break them down into individual browser tool calls. It will:
- Decide which tools to use (navigate, click, screenshot, etc.)
- Execute them in sequence
- Handle errors gracefully
- Provide a summary at the end
