from playwright.sync_api import Page, BrowserContext, expect


def test_tab_navigation(page: Page, context: BrowserContext):
    page.goto('https://www.qa-practice.com/elements/new_tab/button')
    click_btn = page.get_by_role('link', name='Click')

    with context.expect_page() as new_page_event:
        click_btn.click()
    new_tab = new_page_event.value
    expect(new_tab.locator('#result-text')).to_have_text('I am a new page in a new tab')
    new_tab.close()
    expect(click_btn).to_be_enabled()
