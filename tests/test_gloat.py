import pytest
import requests

from selenium import webdriver
from actions import common_actions

browser = webdriver.Chrome()
browser.implicitly_wait(10)
helper = common_actions()

location_names = ["LONDON",
                  "NEW YORK",
                  "TEL AVIV",
                  "MELBOURNE"]
@pytest.mark.parametrize("location", location_names)
def test_check_location_links_are_opened(location):
    helper.get_careers_url(browser)
    helper.enter_location_of_careers(browser, location)
    helper.press_back_to_all_positions(browser)


def test_home_button():
    helper.get_careers_url(browser)
    helper.press_home_button(browser)


def test_assistant_is_opened():
    helper.get_careers_url(browser)
    helper.open_assistant(browser)


@pytest.mark.parametrize("location", location_names)
def test_get_api(location):
    helper.get_careers_url(browser)
    response = requests.get('https://x.gloat.com/careers/{}'.format(location))
    assert response.status_code == 200, "returned status-code is {} !".format(response.status_code)