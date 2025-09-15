from playwright.sync_api import Page, expect


class PracticePage:
    def __init__(self, page: Page):
        self.page = page
        self.radio = page.locator("input[type='radio']")
        self.suggestion = page.locator("#autocomplete")
        self.option = page.locator("#dropdown-class-example option")
        self.checkbox = page.locator("input[type='checkbox']")
        self.window_button = page.locator("#openwindow")
        self.new_tab_button = page.locator("#opentab")
        self.name_field = page.locator("#name")
        self.alert_button = page.locator("#alertbtn")
        self.confirm_button = page.locator("#confirmbtn")
        
        
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
        print("\n")
        checkboxes = self.checkbox
        count = checkboxes.count()
        print("Checkbox found:",count)
        
        for i in range(count):
            checkbox = checkboxes.nth(i)
            checkbox.check()
            print(f"Checked: {checkbox.get_attribute('value')}")
            
    def switch_window_example(self):
        #Switch Window Example
        print("\n")
        open_window_button = self.window_button
    
        with self.page.context.expect_page() as popup_info:
            open_window_button.click()
        new_window = popup_info.value
        new_window.wait_for_load_state()
        new_window.evaluate("""
            window.scrollTo({
                top: document.body.scrollHeight,
                behavior:'smooth'
            })
        """)
        
        print("New Window URL:", new_window.url)
        
    def switch_tab_example(self):
        #Switch Tab Example
        print("\n")
        open_tab_button = self.new_tab_button
        
        with self.page.expect_popup() as popup_info:
            open_tab_button.click()

        new_tab  = popup_info.value
        new_tab.wait_for_load_state()
        print("New Tab URL:", new_tab.url)
        
    def switch_to_alert_example(self):
        #Switch to alert example
        print("\n")
        def handle_prompt(dialog):
            print(f"Prompt detected!")
            print(f"Prompt message: {dialog.message}")
            print(f"Dialog type: {dialog.type}")
            dialog.accept()
            
        name_field = self.name_field
        alert_button = self.alert_button 
        confirm_button = self.confirm_button 

        self.page.on("dialog", handle_prompt)
                
        name_field.fill("AlertButton")
        alert_button.click()
        print("\n")
        name_field.fill("ConfirmButton")
        confirm_button.click()
        
