from playwright.sync_api import Page, expect

def test_template(page: Page):
    checkboxes = page.locator("input[type='checkbox']")
    count = checkboxes.count()
    print("Checkbox found:",count)
    
    for i in range(count):
        checkbox = checkboxes.nth(i)
        checkbox.check()
        print(f"Checked: {checkbox.get_attribute('value')}")