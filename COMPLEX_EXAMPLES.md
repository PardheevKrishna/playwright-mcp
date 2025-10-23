# Complex Interaction Examples
## Ready-to-Run Commands for Testing Complex Browser Automation

---

## 🎯 Form Filling Examples

### Example 1: Simple Contact Form
```powershell
python browser_automation.py "Open the contact form, fill 'John Smith' in the name field, fill 'john.smith@email.com' in the email field, fill 'I would like more information about your services' in the message box, then click the Send button"
```

### Example 2: Registration Form with Dropdowns
```powershell
python browser_automation.py "Go to the signup page, fill 'JohnDoe' in username, fill 'john@example.com' in email, fill 'SecurePass123' in password field, select 'United States' from the country dropdown, select 'New York' from the state dropdown, check the terms and conditions checkbox, then click Register"
```

### Example 3: Multi-Step Form (Wizard)
```powershell
python browser_automation.py "Fill the multi-step form: Step 1 - enter first name 'John', last name 'Doe', click Next. Step 2 - enter email 'john@example.com', phone '555-1234', click Next. Step 3 - select 'Premium' plan from dropdown, check 'Annual billing' checkbox, click Next. Step 4 - review and click Submit"
```

---

## 🛒 E-Commerce Interactions

### Example 4: Product Search and Filter
```powershell
python browser_automation.py "Go to the online store, search for 'wireless headphones', select 'Over-Ear' from type dropdown, select 'Under $100' from price filter, select 'Black' from color options, click Apply Filters, take a screenshot of filtered results"
```

### Example 5: Add to Cart Flow
```powershell
python browser_automation.py "Search for 'laptop backpack', click the first product, select 'Large' from size dropdown, select 'Navy Blue' from color dropdown, set quantity to 2 using the quantity selector, click Add to Cart, wait for confirmation, take a screenshot"
```

### Example 6: Checkout Process (Demo)
```powershell
python browser_automation.py "Go to shopping cart, review items, click Proceed to Checkout, fill shipping form: name 'Jane Doe', address '123 Main St', city 'Springfield', select 'Illinois' from state dropdown, zip '62701', fill phone '555-0123', select 'Standard Shipping' option, take screenshot, click Continue to Payment"
```

---

## 🔍 Search and Filter Operations

### Example 7: Job Search with Filters
```powershell
python browser_automation.py "Go to job board, search for 'Python Developer', select 'Remote' from location dropdown, select 'Full-time' from job type dropdown, select '$80k-$120k' from salary range, check 'With benefits' checkbox, click Search, take screenshot of first 5 results"
```

### Example 8: Real Estate Search
```powershell
python browser_automation.py "Open real estate website, select 'For Sale' from listing type, type 'San Francisco' in location, select '2 Bedrooms' from bedrooms dropdown, select '2 Bathrooms' from bathrooms dropdown, set price range min $500k max $800k, check 'Has parking' checkbox, click Search, take screenshot"
```

---

## 📊 Data Entry and Collection

### Example 9: Survey Completion
```powershell
python browser_automation.py "Fill the survey: Question 1 - select 'Very Satisfied' radio button, Question 2 - select 'Daily' from frequency dropdown, Question 3 - check boxes for 'Quality', 'Price', and 'Service', Question 4 - type 'The product exceeded my expectations' in comment box, Question 5 - select '5 stars' rating, click Submit Survey"
```

### Example 10: Booking Form
```powershell
python browser_automation.py "Fill hotel booking: select check-in date 'Dec 15, 2024', select check-out date 'Dec 20, 2024', select '2 Adults' from guests dropdown, select 'Deluxe Room' from room type dropdown, check 'Breakfast included' checkbox, fill special requests 'Late check-in please', click Check Availability"
```

---

## 🎨 Interactive Element Testing

### Example 11: Accordion and Tabs
```powershell
python browser_automation.py "Open the FAQ page, click the first accordion item to expand it, take a screenshot, click the second accordion to expand, close the first one, take another screenshot, then click the 'Pricing' tab, take a screenshot, click 'Features' tab, take final screenshot"
```

### Example 12: Modal and Popup Interactions
```powershell
python browser_automation.py "Open the page, click 'Learn More' button to open modal dialog, read the content, select 'Send me updates' checkbox in the modal, fill email in the modal popup, click Subscribe in the modal, wait for success message, take screenshot, close the modal"
```

### Example 13: Drag and Drop Builder
```powershell
python browser_automation.py "Open the page builder, drag 'Header' component from left panel to main canvas, drag 'Text Block' below header, drag 'Image' component below text, drag 'Button' at the bottom, take screenshot of the layout, click Preview to see result"
```

---

## 🎯 Advanced Click Interactions

### Example 14: Context Menu (Right-Click)
```powershell
python browser_automation.py "Go to the page, right-click on the image, select 'Save Image As' from context menu, or if that's not available, just take a screenshot of the context menu"
```

### Example 15: Double-Click Actions
```powershell
python browser_automation.py "Open the file manager, double-click the 'Documents' folder to open it, double-click the 'Reports' subfolder, take a screenshot"
```

### Example 16: Hover to Reveal
```powershell
python browser_automation.py "Go to the navigation menu, hover over 'Products' to reveal the dropdown menu, hover over 'Software' in the submenu to reveal third-level items, click 'Cloud Solutions', take a screenshot"
```

---

## 📱 Mobile-Style Interactions

### Example 17: Carousel Navigation
```powershell
python browser_automation.py "Open the product page with image carousel, click the right arrow 3 times to view different images, take a screenshot of each image, then click the thumbnail of the first image to return"
```

### Example 18: Slider Controls
```powershell
python browser_automation.py "Open the filter page, use the price slider to set minimum to $50 and maximum to $200, use the distance slider to set range to 25 miles, take a screenshot of the adjusted filters, click Apply"
```

---

## 🔐 Authentication Flows (Demo Sites Only)

### Example 19: Login Process
```powershell
python browser_automation.py "Go to demo login page, fill 'testuser@example.com' in email field, fill 'TestPassword123' in password field, check 'Remember me' checkbox, click Login button, wait for dashboard to load, take a screenshot"
```

### Example 20: Password Reset Flow
```powershell
python browser_automation.py "Click 'Forgot Password' link, fill email 'user@example.com', click 'Send Reset Link', wait for confirmation message, take screenshot showing 'Email sent' notification"
```

---

## 🎮 Multi-Tab Operations

### Example 21: Compare in Multiple Tabs
```powershell
python browser_automation.py "Open Product A in first tab and take screenshot, open new tab and load Product B and take screenshot, open third tab for Product C and take screenshot, switch back to first tab, provide comparison summary"
```

### Example 22: Research Across Sites
```powershell
python browser_automation.py "Tab 1: Search 'Python tutorials' on Google, Tab 2: Open top result, Tab 3: Open Wikipedia Python page, Tab 4: Open Python official docs, take screenshots of all tabs, summarize the different resources"
```

---

## 🎯 Conditional Interactions

### Example 23: Check and Act
```powershell
python browser_automation.py "Go to the page, if 'Accept Cookies' banner appears then click Accept, then proceed to fill the form with name 'Test User', if terms checkbox exists then check it, click Submit"
```

### Example 24: Error Handling Flow
```powershell
python browser_automation.py "Fill the form with invalid email 'notanemail', click Submit, if error message appears take a screenshot, correct the email to 'valid@email.com', submit again, take screenshot of success"
```

---

## 📊 Table and List Interactions

### Example 25: Sort and Filter Table
```powershell
python browser_automation.py "Open the data table, click the 'Name' column header to sort alphabetically, click the 'Price' column header to sort by price, use the filter dropdown to show only 'In Stock' items, take screenshot of filtered and sorted results"
```

### Example 26: Pagination
```powershell
python browser_automation.py "View the list, take screenshot of page 1, click 'Next' to go to page 2, take screenshot, click 'Next' again for page 3, take screenshot, click 'Previous' to go back, take final screenshot"
```

---

## 🎨 Complex Form Example (All Together)

### Example 27: Complete Application Form
```powershell
python browser_automation.py "Fill the complete job application: 

Section 1 - Personal Info:
- First name: 'Sarah'
- Last name: 'Johnson'  
- Email: 'sarah.j@email.com'
- Phone: '555-0199'
- Select 'United States' from country dropdown
- Select 'California' from state dropdown
- City: 'San Francisco'
- Zip: '94102'

Section 2 - Professional Info:
- Select 'Bachelor Degree' from education dropdown
- Select '5-10 years' from experience dropdown
- Current job title: 'Senior Developer'
- Select 'Software Development' from industry dropdown

Section 3 - Position:
- Select 'Full-time' from position type
- Select 'Remote' from work location
- Select '$100k-$150k' from salary range dropdown
- Check 'Immediate' for start date availability

Section 4 - Additional:
- Upload resume (if possible)
- Check 'Authorize background check' checkbox
- Check 'Agree to terms' checkbox
- Fill additional comments: 'Excited about this opportunity'

Then click Submit Application and take confirmation screenshot"
```

---

## 🎯 Real-World Scenario Examples

### Example 28: Travel Booking Flow
```powershell
python browser_automation.py "Book a flight: select 'Round-trip' radio button, type 'New York' in departure, select 'JFK' from dropdown, type 'Los Angeles' in destination, select 'LAX' from dropdown, click departure date picker and select June 15, click return date picker and select June 22, select '2 passengers' from dropdown, select 'Economy' from class dropdown, click Search Flights, take screenshot of results"
```

### Example 29: Event Registration
```powershell
python browser_automation.py "Register for conference: select 'Professional' from ticket type dropdown, set quantity to 1, click Continue, fill attendee name 'Michael Brown', email 'michael@email.com', company 'Tech Corp', job title 'Engineer', select 'Technology' from industry dropdown, check dietary restrictions 'Vegetarian', select 'Yes' for newsletter, click Proceed to Payment"
```

### Example 30: Restaurant Order
```powershell
python browser_automation.py "Order food online: select 'Delivery' option, type address '456 Oak Avenue', select 'Italian' from cuisine dropdown, click search, select first restaurant, click 'Pasta' category, select 'Spaghetti Carbonara', select 'Large' from size dropdown, check 'Extra cheese' checkbox, set quantity to 2, click Add to Cart, click Checkout, select delivery time '6:00 PM', add special instructions 'Ring doorbell', take screenshot"
```

---

## 🎓 Testing Your Own Sites

### Template for Form Testing
```powershell
python browser_automation.py "Go to [YOUR_SITE_URL], fill [FIELD_NAME] with [VALUE], select [OPTION] from [DROPDOWN_NAME] dropdown, check [CHECKBOX_NAME] checkbox, click [BUTTON_NAME] button, take screenshot"
```

### Template for Navigation Testing  
```powershell
python browser_automation.py "Open [URL], click [LINK_TEXT], wait 2 seconds, click [BUTTON], take screenshot, go back, click [DIFFERENT_LINK], take final screenshot"
```

---

## 💡 Pro Tips

1. **Always specify exact element descriptions**: "the blue Submit button" not just "button"
2. **Add waits for dynamic content**: "wait 2 seconds after clicking"
3. **Take screenshots at key steps**: helps debug and verify
4. **Test incrementally**: start simple, then add complexity
5. **Use clear dropdown option names**: exactly as they appear on screen
6. **Check elements exist before interaction**: "if the modal is open, click close"

---

## 🚀 Start Testing!

Pick any example above, replace placeholder values with real data if needed, and run:

```powershell
python browser_automation.py "YOUR_INSTRUCTION_HERE"
```

Watch the browser window as it executes each step! The visible (headed) mode lets you see exactly what's happening.

---

## 📚 Next Steps

1. Try the simple examples first (Examples 1-5)
2. Move to filtering and selection (Examples 6-10)
3. Test interactive elements (Examples 11-15)
4. Practice complex multi-step flows (Examples 27-30)
5. Create your own custom automation scenarios!

Happy automating! 🎉
