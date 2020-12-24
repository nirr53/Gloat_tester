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
        # assistant
        browser.find_element_by_xpath('/html/body/div[2]/div/div[1]').click()



# <div class="intercom-lightweight-app-launcher-icon intercom-lightweight-app-launcher-icon-open"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 28 32"><path d="M28 32s-4.714-1.855-8.527-3.34H3.437C1.54 28.66 0 27.026 0 25.013V3.644C0 1.633 1.54 0 3.437 0h21.125c1.898 0 3.437 1.632 3.437 3.645v18.404H28V32zm-4.139-11.982a.88.88 0 00-1.292-.105c-.03.026-3.015 2.681-8.57 2.681-5.486 0-8.517-2.636-8.571-2.684a.88.88 0 00-1.29.107 1.01 1.01 0 00-.219.708.992.992 0 00.318.664c.142.128 3.537 3.15 9.762 3.15 6.226 0 9.621-3.022 9.763-3.15a.992.992 0 00.317-.664 1.01 1.01 0 00-.218-.707z"></path></svg></div>

# <div class="intercom-lightweight-app-launcher intercom-launcher" role="button" tabindex="0" aria-label="Open Intercom Messenger"><div class="intercom-lightweight-app-launcher-icon intercom-lightweight-app-launcher-icon-open"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 28 32"><path d="M28 32s-4.714-1.855-8.527-3.34H3.437C1.54 28.66 0 27.026 0 25.013V3.644C0 1.633 1.54 0 3.437 0h21.125c1.898 0 3.437 1.632 3.437 3.645v18.404H28V32zm-4.139-11.982a.88.88 0 00-1.292-.105c-.03.026-3.015 2.681-8.57 2.681-5.486 0-8.517-2.636-8.571-2.684a.88.88 0 00-1.29.107 1.01 1.01 0 00-.219.708.992.992 0 00.318.664c.142.128 3.537 3.15 9.762 3.15 6.226 0 9.621-3.022 9.763-3.15a.992.992 0 00.317-.664 1.01 1.01 0 00-.218-.707z"></path></svg></div><div class="intercom-lightweight-app-launcher-icon intercom-lightweight-app-launcher-icon-minimize"><svg viewBox="0 0 16 14" xmlns="http://www.w3.org/2000/svg"><path fill-rule="evenodd" clip-rule="evenodd" d="M.116 4.884l1.768-1.768L8 9.232l6.116-6.116 1.768 1.768L8 12.768.116 4.884z"></path></svg></div></div>
