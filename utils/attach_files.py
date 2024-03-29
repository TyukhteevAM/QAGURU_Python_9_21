import os

import allure
import requests
from dotenv import load_dotenv
from selene import browser


load_dotenv()
user_name = os.environ.get('USER_NAME')
password = os.environ.get('ACCESS_KEY')


def attach_bstack_video(session_id):
    bstack_session = requests.get(
        f'https://api.browserstack.com/app-automate/sessions/{session_id}.json',
        auth=(user_name, password),
    ).json()

    video_url = bstack_session['automation_session']['video_url']

    allure.attach(
        '<html><body>'
        '<video width="100%" height="100%" controls autoplay>'
        f'<source src="{video_url}" type="video/mp4">'
        '</video>'
        '</body></html>',
        name='video recording',
        attachment_type=allure.attachment_type.HTML,
    )


def attach_screenshot():
    allure.attach(
        browser.driver.get_screenshot_as_png(),
        name='screenshot',
        attachment_type=allure.attachment_type.PNG,
    )
