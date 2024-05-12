from playwright.sync_api import Page, Locator, expect


class BasePage:
    base_url = 'https://magento.softwaretestingboard.com'
    page_path = None
    accept_cookie_btn_loc = 'button.fc-cta-consent'
    page_is_loaded_trigger_element = '.not-logged-in'

    def __init__(self, page: Page):
        self.page = page

    def open_page(self):
        self.page.goto(f'{self.base_url}{self.page_path}')
        self.page_is_load()

    def page_is_load(self):
        expect(self.find(self.page_is_loaded_trigger_element)).to_be_visible()

    def find(self, locator_str) -> Locator:
        return self.page.locator(locator_str).first

    def find_all(self, locator_str):
        return self.page.locator(locator_str)
