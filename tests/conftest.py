import allure
import pytest
from appium.options.ios import XCUITestOptions
from appium.options.android import UiAutomator2Options
from selene import browser
from appium import webdriver

from settings import config
from utils import attach_files


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

            "userName": config.user_name,
            "accessKey": config.access_key,
        }
    })

    browser.config.driver = webdriver.Remote("http://hub.browserstack.com/wd/hub", options=options)

    yield

    attach_files.attach_screenshot()
    session_id = browser.driver.session_id

    with allure.step('Add attach_files'):
        browser.quit()

    attach_files.attach_bstack_video(session_id)


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

            "userName": config.user_name,
            "accessKey": config.access_key,
        }
    })

    browser.config.driver = webdriver.Remote("http://hub.browserstack.com/wd/hub", options=options)

    yield

    attach_files.attach_screenshot()
    session_id = browser.driver.session_id

    with allure.step('Add attach_files'):
        browser.quit()

    attach_files.attach_bstack_video(session_id)
