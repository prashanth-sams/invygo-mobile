import pytest
from src.helpers.appiumdriver import Driver
from src.screens.car_specs_screen import CarSpecsScreen
from src.helpers.app import App
from appium.webdriver.common.appiumby import AppiumBy
from src.helpers.constants import *


class TestCarSpecs(Driver):
    
    def __init__(self, driver):
        super().__init__(driver)

    """
    This test case is to verify the car specs page
    """
    @pytest.mark.specs
    def test_carspecs(self):
        self.driver.get(BASE_URL + "/car-specs")
        
        all_cars = App.elements(self, CarSpecsScreen.all_cars)

        for i in range(len(all_cars)):
            self.driver.find_elements(AppiumBy.XPATH, '//*[contains(text(), "Learn More")]')[i].click()
            
            App.is_displayed(self, CarSpecsScreen.monthly_plans, True)
            self.driver.back()
            App.is_displayed(self, CarSpecsScreen.specs_bg, True)
    