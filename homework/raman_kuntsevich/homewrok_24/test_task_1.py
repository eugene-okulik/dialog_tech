from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.alert import Alert


def test_add_to_cart(driver):
    wait = WebDriverWait(driver, 5)
    control_btn = Keys.CONTROL
    driver.get('https://www.demoblaze.com/index.html')

    products = driver.find_elements(By.XPATH, '//div[@id="tbodyid"]//div[contains(@class, "card")]')
    first_product = products[0]
    product_title = first_product.find_element(By.TAG_NAME, 'h4')
    product_title_text = product_title.text
    product_price_text = first_product.find_element(By.TAG_NAME, 'h5').text.replace('$', '')
    actions = ActionChains(driver)
    actions.key_down(control_btn)
    actions.click(product_title)
    actions.key_up(control_btn)
    actions.perform()
    tabs = driver.window_handles
    driver.switch_to.window(tabs[1])

    add_to_cart_btn_selector = (By.CSS_SELECTOR, '[onclick="addToCart(1)"]')
    wait.until(EC.visibility_of_element_located(add_to_cart_btn_selector))
    driver.find_element(*add_to_cart_btn_selector).click()
    wait.until(EC.alert_is_present())
    alert = Alert(driver)
    alert.accept()

    driver.close()
    driver.switch_to.window(tabs[0])

    cart_btn = driver.find_element(By.ID, 'cartur')
    cart_btn.click()

    products_in_cart_selector = (By.XPATH, '//tbody[@id="tbodyid"]//tr[@class="success"]')
    wait.until(EC.visibility_of_element_located(products_in_cart_selector))
    added_product = driver.find_elements(*products_in_cart_selector)[0]
    card_product_title = added_product.find_elements(By.TAG_NAME, 'td')[1]
    card_product_price = added_product.find_elements(By.TAG_NAME, 'td')[2]
    assert product_title_text == card_product_title.text
    assert product_price_text == card_product_price.text
