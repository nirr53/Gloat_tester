# Gloat_tester
Project for Gloat first interview, using Pytest as tests framework, Selenium as GUI testing driver.
The project is written with Pythin 3.7

Configuration:

1. On terminal,
      gh repo clone nirr53/Gloat_tester
   to clone the project.
   
2. On terminal set the Selenium, Pytest and Requests plugins, using:
      pip3 install selenium
      pip3 install pytest
      pip3 install requests
      
3.
  1. Download a Selenium driver from:
    https://chromedriver.chromium.org/downloads
  2. On gloat_data.properties, set the chrome_drv_path to the location of the Chrome driver


4. To run the tests set:
    python3.7 -m pytest --jira  -v -s test_gloat.py
