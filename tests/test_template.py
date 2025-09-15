from playwright.sync_api import Page, expect

def test_template(page: Page):
    #Element display example
    hide_button = page.locator("#hide-textbox")
    show_button = page.locator("#show-textbox")
    input_field = page.locator("#displayed-text")
    value = input_field.text_content()

    input_field.fill("Teste123456")
    
    if input_field.is_visible():
        expect(input_field).to_be_visible()
        print("Input field is visible")
        print("Input field value:", value)
    elif input_field.is_hidden():
        expect(input_field).to_be_hidden()
        print("Input field is hidden")
    else: 
        print("No input field found")