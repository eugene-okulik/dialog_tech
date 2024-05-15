from playwright.sync_api import expect
from test_UI_rkuntsevich_pw.pages.base_page import BasePage
from test_UI_rkuntsevich_pw.pages.locators import sale_locators as loc
import re


class SalePage(BasePage):
    page_path = '/sale.html'

    def check_header(self):
        header = 'Sale'
        page_header = self.find(loc.page_title_loc)

        expect(page_header).to_have_text(header)

    def check_sidebar_section_titles(self):
        section_titles = ["Women's Deals", "Mens's Deals", 'Gear Deals']
        sidebar_section_titles_elements = self.find_all(loc.sidebar_section_titles_loc)

        expect(sidebar_section_titles_elements).to_have_text(section_titles)

    def check_menu_tab_is_active(self):
        sale_menu_tab = self.find(loc.sale_menu_tab_loc)
        expect(sale_menu_tab).to_have_attribute('class', re.compile('active'))
