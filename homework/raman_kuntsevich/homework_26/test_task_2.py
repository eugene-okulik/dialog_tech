from playwright.sync_api import Page
from time import sleep


def test_fill_in_form(page: Page):
    page.set_viewport_size({'width': 1920, 'height': 1080})
    page.goto('https://demoqa.com/automation-practice-form')

    first_name = page.get_by_placeholder('First Name')
    first_name.fill("Raman")

    last_name = page.get_by_placeholder('Last Name')
    last_name.fill("Kuntsevich")

    email = page.get_by_placeholder('name@example.com')
    email.fill('gotestweb@gmail.com')

    gender = page.locator('//label[text()="Male"]/../input')
    gender.check(force=True)

    mobile = page.get_by_placeholder('Mobile Number')
    mobile.fill('1234567890')

    subjects = page.locator('#subjectsInput')
    subjects.fill('a')
    subjects.press('Enter')

    hobbies = page.locator('//label[text()="Music"]/../input')
    hobbies.check(force=True)

    address = page.get_by_role('textbox', name='Current Address')
    address.fill("Bla bla bla street")

    state = page.locator('#react-select-3-input')
    state.fill('a')
    state.press('Enter')

    city = page.locator('#react-select-4-input')
    city.fill('a')
    city.press('Enter')

    submit_btn = page.get_by_role('button', name='Submit')
    submit_btn.click()
