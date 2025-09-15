from playwright.sync_api import Page, expect

def test_template(page: Page):
    #Switch Window Example
    open_window_button = page.locator("#openwindow")
    
    with page.context.expect_page() as popup_info:
        open_window_button.click()
    new_window = popup_info.value
    new_window.wait_for_load_state()
    new_window.evaluate("""
        window.scrollTo({
            top: document.body.scrollHeight,
            behavior:'smooth'
        })
     """)
    
    print(new_window.url)
    
    
    page.wait_for_timeout(3000)