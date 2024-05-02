from selenium.webdriver.common.by import By
from faker import Faker
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random


def test_send_form(driver):
    wait = WebDriverWait(driver, 5)
    driver.get('https://demoqa.com/automation-practice-form')

    first_name_field = driver.find_element(By.ID, 'firstName')
    first_name_field.send_keys('Raman')

    last_name_field = driver.find_element(By.ID, 'lastName')
    last_name_field.send_keys('Kuntsevich')

    email_field = driver.find_element(By.ID, 'userEmail')
    email_field.send_keys('gotestweb@gmail.com')

    gender_radio_buttons = driver.find_elements(By.XPATH, '//input[@name="gender"]/..')
    gender_radio = random.choice(gender_radio_buttons)
    gender_radio.click()

    phone_field = driver.find_element(By.ID, 'userNumber')
    phone_field.send_keys('0123456789')

    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    date_field = driver.find_element(By.ID, 'dateOfBirthInput')
    date_field.click()

    year_select = Select(driver.find_element(By.CSS_SELECTOR, '.react-datepicker__year-select'))
    year_select.select_by_index(random.randint(0, len(year_select.options) - 1))

    month_select = Select(driver.find_element(By.CSS_SELECTOR, '.react-datepicker__month-select'))
    month_select.select_by_index(random.randint(0, len(month_select.options) - 1))

    day_picker = driver.find_elements(By.CSS_SELECTOR, '.react-datepicker__day')
    day = random.choice(day_picker)
    day.click()

    subjects_field = driver.find_element(By.ID, 'subjectsInput')
    subjects_field.send_keys('a')
    subjects_field.send_keys(Keys.ENTER)

    hobbies_checkboxes = driver.find_elements(By.XPATH, '//input[contains(@id, "hobbies-checkbox")]/..')
    hobby_checkbox = random.choice(hobbies_checkboxes)
    hobby_checkbox.click()

    address_field = driver.find_element(By.ID, 'currentAddress')
    address_field.send_keys(Faker().address())

    state = driver.find_element(By.ID, 'react-select-3-input')
    state.send_keys('a')
    state.send_keys(Keys.ENTER)

    city_locator = (By.ID, 'react-select-4-input')
    city = driver.find_element(*city_locator)
    wait.until(EC.element_to_be_clickable(city_locator))
    city.send_keys('a')
    city.send_keys(Keys.ENTER)

    submit_button = driver.find_element(By.ID, 'submit')
    submit_button.click()

    result_table_locator = (By.CSS_SELECTOR, 'table.table')
    wait.until(EC.presence_of_element_located(result_table_locator))
    print(driver.find_element(*result_table_locator).text)
