import pytest
from playwright.sync_api import BrowserContext
from test_UI_rkuntsevich_pw.pages.sale_page import SalePage
from test_UI_rkuntsevich_pw.pages.registration_page import RegistrationPage
from test_UI_rkuntsevich_pw.pages.eco_friendly_page import EcoFriendlyPage


@pytest.fixture()
def page(context: BrowserContext):
    page = context.new_page()
    page.set_viewport_size({'width': 1920, 'height': 1080})

    return page


@pytest.fixture()
def sale_page(page) -> SalePage:
    return SalePage(page)


@pytest.fixture()
def registration_page(page) -> RegistrationPage:
    return RegistrationPage(page)


@pytest.fixture()
def eco_friendly_page(page) -> EcoFriendlyPage:
    return EcoFriendlyPage(page)
