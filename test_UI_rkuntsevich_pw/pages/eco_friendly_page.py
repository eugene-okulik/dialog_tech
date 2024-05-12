from playwright.sync_api import expect
import re

from test_UI_rkuntsevich_pw.pages.base_page import BasePage
from test_UI_rkuntsevich_pw.pages.locators import eco_friendly_locators as loc


class EcoFriendlyPage(BasePage):
    page_path = '/collections/eco-friendly.html'

    def check_product_names(self):
        product_names_elements = self.get_product_names()
        expect(product_names_elements).to_contain_text([re.compile('.*')])

    def get_product_names(self):
        return self.find_all(loc.product_names_loc)

    def get_product_prices(self):
        return self.find_all(loc.product_prices_loc)

    def change_product_grid_mode(self, grid_mode):
        grid_mode_btn = self.find(loc.grid_btn_loc)
        list_mode_btn = self.find(loc.list_btn_loc)

        if grid_mode == 'list':
            list_mode_btn.click()
        elif grid_mode == 'grid':
            grid_mode_btn.click()

        self.page_is_load()

    def change_sorting_type(self, value):
        sort_select = self.find(loc.sort_select_loc)
        sort_select.select_option(value)

    def change_sorting_order(self, sort_order):
        sort_action = self.find(loc.sorter_action_loc)

        if sort_action.get_attribute('data-value') != sort_order:
            sort_action.click()

    def check_sort_by_name(self, sort_order):
        product_names = self.get_product_names()
        product_names_text = list([element.text_content() for element in product_names.all()])
        sorted_names_text = sorted(product_names_text, reverse=True if sort_order == 'asc' else False)
        expect(product_names).to_have_text(sorted_names_text)

    def check_sort_by_price(self, sort_order):
        product_prices = self.get_product_prices()
        product_prices_nums = list([element.text_content() for element in product_prices.all()])
        sorted_prices = sorted(
            product_prices_nums,
            reverse=True if sort_order == 'asc' else False)
        expect(product_prices).to_have_text(sorted_prices)

    def sort_products(self, sort_type, sort_order):
        self.change_sorting_type(sort_type)
        self.page_is_load()
        self.change_sorting_order(sort_order)
