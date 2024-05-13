from appium import webdriver
import unittest
import os
from datetime import datetime
import pytest
from pytest_html_reporter import attach
from appium.options.common import AppiumOptions
from src.helpers.constants import *
from src.helpers.desired_capabilities import get_desired_capabilities


class Driver(unittest.TestCase):

    def __init__(self, driver):
        super().__init__(driver)

    def setUp(self):
        """
        This method instantiates the appium driver
        """
        self.logger.info("Initiating Appium driver")
        
        caps = get_desired_capabilities()
        self.driver = webdriver.Remote(SERVER_URL_BASE, options=AppiumOptions().load_capabilities(caps))

        self.driver.implicitly_wait(5)  # waits 5 seconds
    
    def tearDown(self):
        """
        This method is called after each test method has run
        """
        self.logger.info("Tearing down Appium driver")
        
        attach(data=self.driver.get_screenshot_as_png())
        self.driver.quit()
            
    def screenshot_on_failure(self):
        self.logger.info("Taking screenshot on failure")
        
        now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
        test_name = self._testMethodName
        for self._testMethodName, error in self._outcome.errors:
            if error:
                self.logger.error("Taking screenshot on failure")
                if not os.path.exists('screenshots'):
                    os.makedirs('screenshots')

                self.driver.save_screenshot(f"screenshots/{test_name}_{now}.png")

    @pytest.fixture(autouse=True)
    def cli(self, app, device, get_logger):
        self.app = app
        self.device = device
        self.logger = get_logger


if __name__ == '__main__':
    unittest.main()
