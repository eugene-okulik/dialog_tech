from playwright.sync_api import Page


def test_login(page: Page):
    page.goto('https://the-internet.herokuapp.com/')
    page.get_by_role('link', name='Form Authentication').click()
    username = page.get_by_role('textbox', name='username')
    username.fill('testUserName')
    password = page.get_by_role('textbox', name='password')
    password.fill('testPassword')
    submit_btn = page.get_by_role('button', name=' Login')
    submit_btn.click()
