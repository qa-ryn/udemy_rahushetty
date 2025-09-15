from playwright.sync_api import Page, expect


class PracticePage:
    def __init__(self, page: Page):
        self.page = page
        self.radio = page.locator("input[type='radio']")
        self.suggestion = page.locator("#autocomplete")
        self.option = page.locator("#dropdown-class-example option")
        self.checkbox = page.locator("input[type='checkbox']")
        
        
    def radio_button_example(self):
        radio_buttons = self.radio

        count = radio_buttons.count()
        print("Radio Button Found:", count)
        
        for i in range(count):
            radio = radio_buttons.nth(i)
            
            #get label text (radio buttons are insdie <label>)
            label_text = radio.locator("xpath=..").inner_text().strip()
            
            #check the radion button
            radio.check()
            expect(radio).to_be_checked()
            
            #print label text
            print(label_text)

    def suggestion_class_example(self):
        #suggestion Class
        print("\n")
        suggestion_input = self.suggestion
        suggestion_input.fill("br")
        
        self.page.wait_for_selector("[id^='ui-id']")

        # Get all suggestion items (only li children, not the parent wrapper)
        items = self.page.locator("ul.ui-autocomplete li")
        count = items.count()

        suggestion_list = []
        for i in range(count):
            text = items.nth(i).inner_text().strip()
            suggestion_list.append(text)

        print("Suggestions:")
        for idx, item in enumerate(suggestion_list, start=1):
            print(f" {idx}) {item}")
            
    def dropdown_example(self):
        #dropdown example 
        print("\n")
        options = self.option
        count = options.count()
        print(f"Dropdown has {count} options:")

        # Loop through each option
        for i in range(count):
            option = options.nth(i)
            text = option.inner_text().strip()
            value = option.get_attribute("value")

            print(f"Selecting -> {text} (value='{value}')")

            # Select the option (skip empty value for "Select")
            if value:
                self.page.select_option("#dropdown-class-example", value=value)

                # Verify selection
                selected_value = self.page.locator("#dropdown-class-example").input_value()
                print(f"   ✅ Selected: {selected_value}")
                
    def checkbox_example(self):
        checkboxes = self.checkbox
        count = checkboxes.count()
        print("Checkbox found:",count)
        
        for i in range(count):
            checkbox = checkboxes.nth(i)
            checkbox.check()
            print(f"Checked: {checkbox.get_attribute('value')}")