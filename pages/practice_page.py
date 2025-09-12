from playwright.sync_api import Page, expect


class PracticePage:
    def __init__(self, page: Page):
        self.page = page
        self.radio = page.locator("input[type='radio']")
        
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