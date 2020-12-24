from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

from base_functions import ConfigFile

config = ConfigFile()
config.set_config_file("gloat_data.properties")
CHROME_DRV_PATH   = config.get_as_string('UI', 'chrome_drv_path')
GLOAT_CAREERS_URL = config.get_as_string('UI', 'gloat_careers_url')
GLOAT_HOME_URL    = config.get_as_string('UI', 'gloat_home_url')


class common_actions:
    def __init__(self):
        pass

    def get_careers_url(self, browser):
        browser.get(GLOAT_CAREERS_URL)

    def enter_location_of_careers(self, browser, location):
        browser.find_element_by_partial_link_text(location).click()
        try:
            WebDriverWait(browser, 3).until(EC.presence_of_element_located((By.XPATH, "//*[@id='main-app-container']/div/div/div[""1]/div[1]/div[1]/h1")))
            _location = browser.find_element_by_xpath("//*[@id='main-app-container']/div/div/div[1]/div[1]/div[1]/h1").text
            assert _location.lower() in location.lower()
        except TimeoutException:
            assert False, "Loading took too much time!"

    def press_back_to_all_positions(self, browser):
        browser.find_element_by_partial_link_text("Back to all positions").click()
        try:
            WebDriverWait(browser, 3).until(EC.presence_of_element_located((By.TAG_NAME, "H1")))
            _header = browser.find_element_by_tag_name("H1").text
            assert "Join the team" in _header
        except TimeoutException:
            assert False, "Loading took too much time!"

    def press_home_button(self, browser):
        browser.find_element_by_xpath('//a[@href="' + GLOAT_HOME_URL + '"]').click()
        try:
            WebDriverWait(browser, 3).until(EC.presence_of_element_located((By.TAG_NAME, "H2")))
            _header = browser.find_element_by_tag_name("H2").text
            assert "Create an\nagile workforce" in _header
        except TimeoutException:
            assert False, "Loading took too much time!"

    def open_assistant(self, browser):
        browser.find_element_by_xpath('/html/body/div[2]/div/div[1]').click()
