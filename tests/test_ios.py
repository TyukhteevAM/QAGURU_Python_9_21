from allure_commons._allure import step
from appium.webdriver.common.appiumby import AppiumBy
from selene import browser, have, be


def test_ios_search_wiki_appium(mobile_management_ios):
    with step('Type search'):
        browser.element((AppiumBy.ACCESSIBILITY_ID, "Text Button")).click()
        browser.element((AppiumBy.ACCESSIBILITY_ID, "Text Input")).type("I'm russian" + "\n")
    with step('Verify content found'):
        result = browser.element((AppiumBy.ACCESSIBILITY_ID, "Text Output")).should(be.clickable)
        result.should(have.text("I'm russian"))
