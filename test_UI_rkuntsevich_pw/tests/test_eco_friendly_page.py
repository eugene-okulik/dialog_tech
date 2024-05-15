import pytest


@pytest.mark.smoke
def test_products_have_names(eco_friendly_page):
    eco_friendly_page.open_page()
    eco_friendly_page.check_product_names()


@pytest.mark.regression
@pytest.mark.parametrize('sorting', [
    ('grid', 'desc'),
    ('grid', 'asc'),
    ('list', 'desc'),
    ('list', 'asc')
])
def test_sort_products_by_name(eco_friendly_page, sorting):
    eco_friendly_page.open_page()
    eco_friendly_page.change_product_grid_mode(sorting[0])
    eco_friendly_page.sort_products('name', sorting[1])
    eco_friendly_page.check_sort_by_name(sorting[1])


@pytest.mark.regression
@pytest.mark.parametrize('sorting', [
    ('grid', 'desc'),
    ('grid', 'asc'),
    ('list', 'desc'),
    ('list', 'asc')
])
def test_sort_products_by_price(eco_friendly_page, sorting):
    eco_friendly_page.open_page()
    eco_friendly_page.change_product_grid_mode(sorting[0])
    eco_friendly_page.sort_products('price', sorting[1])
    eco_friendly_page.check_sort_by_price(sorting[1])
