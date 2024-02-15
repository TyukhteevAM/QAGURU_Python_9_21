import os
import pytest
from appium.options.ios import XCUITestOptions
from dotenv import load_dotenv
from appium.options.android import UiAutomator2Options
from selene import browser
from appium import webdriver


load_dotenv()
user_name = os.environ.get('USER_NAME')
password = os.environ.get('ACCESS_KEY')


@pytest.fixture(scope='function')
def mobile_management_android():
    options = UiAutomator2Options().load_capabilities({
        "platformName": "android",
        "platformVersion": "9.0",
        "deviceName": "Google Pixel 3",

        "app": "bs://sample.app",

        'bstack:options': {
            "projectName": "First Python project",
            "buildName": "browserstack-build-1",
            "sessionName": "BStack first_test",

            "userName": user_name,
            "accessKey": password
        }
    })

    browser.config.driver = webdriver.Remote("http://hub.browserstack.com/wd/hub", options=options)

    yield

    browser.quit()


@pytest.fixture(scope='function')
def mobile_management_ios():
    options = XCUITestOptions().load_capabilities({
        "deviceName": "iPhone 14 Pro Max",
        "platformName": "ios",
        "platformVersion": "16",

        "app": "bs://sample.app",

        'bstack:options': {
            "projectName": "First Python project1",
            "buildName": "browserstack-build-1-2",
            "sessionName": "BStack first_test-1",

            "userName": user_name,
            "accessKey": password
        }
    })

    browser.config.driver = webdriver.Remote("http://hub.browserstack.com/wd/hub", options=options)

    yield

    browser.quit()
