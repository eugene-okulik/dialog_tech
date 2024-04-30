from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random


def test_choose_language(driver):
    driver.get('https://www.qa-practice.com/elements/select/single_select')

    language_dropdown = Select(driver.find_element(By.CSS_SELECTOR, 'select#id_choose_language'))
    dropdown_options = language_dropdown.options
    languages = []
    for option in dropdown_options:
        languages.append(option.text)
    languages = list(filter(lambda element: element != '', languages))
    random_language = random.choice(languages)
    language_dropdown.select_by_visible_text(random_language)
    submit_button = driver.find_element(By.ID, 'submit-id-submit')
    submit_button.click()
    result_text = driver.find_element(By.ID, 'result-text')
    assert result_text.text == random_language


def test_dynamic_element(driver):
    wait = WebDriverWait(driver, 10)
    driver.get('https://the-internet.herokuapp.com/dynamic_loading/2')

    start_button = driver.find_element(By.XPATH, '//button[text()="Start"]')
    start_button.click()
    wait.until(EC.visibility_of_element_located((By.ID, 'loading')))
    wait.until(EC.visibility_of_element_located((By.ID, 'finish')))
    finish_text = driver.find_element(By.ID, 'finish').text
    assert finish_text == 'Hello World!'
