from playwright.sync_api import Page
from pages.practice_page import PracticePage

def test_practice_page(page: Page):
    run = PracticePage(page)
    run.radio_button_example()
    
    
    