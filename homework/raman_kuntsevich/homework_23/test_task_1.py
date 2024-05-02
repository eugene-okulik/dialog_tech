from selenium.webdriver.common.by import By
from faker import Faker

TEST_TEXT = Faker().word()


def test_send_field_text(driver):
    driver.get("https://www.qa-practice.com/elements/input/simple")
    text_field = driver.find_element(By.ID, 'id_text_string')
    text_field.send_keys(TEST_TEXT)
    text_field.submit()
    result_text = driver.find_element(By.ID, 'result-text')
    print(result_text.text)
