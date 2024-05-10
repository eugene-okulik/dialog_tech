from playwright.sync_api import Page, expect


def test_wait_button_changed(page: Page):
    page.goto('https://demoqa.com/dynamic-properties')
    color_change_btn = page.locator('#colorChange')
    expect(color_change_btn).to_have_css('color', 'rgb(220, 53, 69)')
    color_change_btn.click()
