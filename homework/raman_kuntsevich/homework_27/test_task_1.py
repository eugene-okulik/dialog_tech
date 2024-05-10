from playwright.sync_api import Page, expect


def test_close_alert(page: Page):
    page.on('dialog', lambda alert: alert.accept())

    page.goto('https://www.qa-practice.com/elements/alert/confirm')
    page.get_by_role('link', name='Click').click()
    expect(page.locator('#result-text')).to_have_text('Ok')
