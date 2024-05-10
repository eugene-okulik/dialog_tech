from playwright.sync_api import Page, expect, Route
from time import sleep
import re
import json


def test_apple_page(page: Page):
    def change_response(route: Route):
        response = route.fetch()
        body = response.json()
        body["body"]["digitalMat"][0]["familyTypes"][0]["productName"] = "яблокофон 15 про"
        body = json.dumps(body)
        route.fulfill(
            response=response,
            body=body
        )

    page.route(re.compile('/step0_iphone/digitalmat'),
               change_response)

    page.goto('https://www.apple.com/shop/buy-iphone')
    button = page.get_by_role('button', name='Take a closer look').locator('nth=0')
    button.click()
    pop_up_header = page.locator('#rf-digitalmat-overlay-label-0').locator('nth=0')
    expect(pop_up_header).to_have_text('яблокофон 15 про')
    sleep(5)
