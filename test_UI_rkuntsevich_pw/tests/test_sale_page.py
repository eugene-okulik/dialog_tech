import pytest


@pytest.mark.smoke
def test_page_header(sale_page):
    sale_page.open_page()
    sale_page.check_header()


@pytest.mark.smoke
def test_sidebar_titles(sale_page):
    sale_page.open_page()
    sale_page.check_sidebar_section_titles()


@pytest.mark.smoke
def test_sale_menu_tab_is_active(sale_page):
    sale_page.open_page()
    sale_page.check_menu_tab_is_active()
