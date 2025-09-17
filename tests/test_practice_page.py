from playwright.sync_api import Page
from pages.practice_page import PracticePage

def test_practice_page(page: Page):
    run = PracticePage(page)
    run.radio_button_example()
    run.suggestion_class_example()
    run.dropdown_example()
    run.checkbox_example()
    run.switch_window_example()
    run.switch_tab_example()
    run.switch_to_alert_example()
    run.element_display_example()
    run.web_table_example()
    run.web_table_fixed_header_example()
    run.mouser_hover_example()
    run.iframe_example()