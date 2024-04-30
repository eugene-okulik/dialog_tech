import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture()
def driver():
    options = Options()
    options.add_argument('start-maximized')
    # options.add_argument('--headless')
    chrome_driver = webdriver.Chrome(options=options)
    chrome_driver.implicitly_wait(2)
    return chrome_driver
