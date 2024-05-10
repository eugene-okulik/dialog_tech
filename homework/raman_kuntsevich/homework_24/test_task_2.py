from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


def test_compare_products(driver):
    wait = WebDriverWait(driver, 5)
    driver.get('https://magento.softwaretestingboard.com/gear/bags.html')

    driver.find_element(By.CSS_SELECTOR, 'button.fc-cta-consent').click()

    products = driver.find_elements(By.CLASS_NAME, 'product-item')
    first_product = products[0]
    first_product_name = first_product.find_element(By.CLASS_NAME, 'name').text
    first_product_compare_btn = first_product.find_element(By.CLASS_NAME, 'tocompare')
    actions = ActionChains(driver)
    actions.move_to_element(first_product)
    actions.click(first_product_compare_btn)
    actions.perform()

    wait.until(EC.visibility_of_element_located((By.ID, 'compare-items')))
    products_to_compare = driver.find_elements(By.XPATH,
                                               '//ol[@id="compare-items"]//strong[@class="product-item-name"]')
    first_product_to_compare = products_to_compare[0]
    assert first_product_to_compare.text == first_product_name
