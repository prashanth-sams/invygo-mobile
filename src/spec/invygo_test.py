import pytest
from src.screens.weekly_subscription_screen import WeeklySubscriptionScreen
from src.helpers.appiumdriver import Driver
from src.screens.monthly_subscription_screen import MonthlySubscriptionScreen
from src.screens.car_details_screen import CarDetailsScreen
from src.helpers.app import App
from src.helpers.constants import *
from src.screens.car_specs_screen import CarSpecsScreen
from appium.webdriver.common.appiumby import AppiumBy


class TestSubscription(Driver):
    
    def __init__(self, driver):
        super().__init__(driver)
    
    
    """
    This test case is to verify the monthly subscription
    """
    @pytest.mark.subscription
    def test_monthly_subscription(self):
        self.driver.get(BASE_URL + "/dubai/monthly-subscription/")
        
        MonthlySubscriptionScreen.filter_car(self)
        
        App.is_displayed(self, CarDetailsScreen.contract_length, True)
        
        CarDetailsScreen.subscribe(self)
        App.is_displayed(self, CarDetailsScreen.popup_header, True)
        App.is_displayed(self, CarDetailsScreen.disabled_continue_button, True)


    """
    This test case is to verify the weekly subscription
    """
    @pytest.mark.subscription
    def test_weekly_subscription(self):
        self.driver.get(BASE_URL + "/dubai/weekly-subscription/")
        
        WeeklySubscriptionScreen.filter_car(self)
        
        App.is_displayed(self, CarDetailsScreen.contract_length, True)
        
        CarDetailsScreen.subscribe(self)
        App.is_displayed(self, CarDetailsScreen.popup_header, True)
        App.is_displayed(self, CarDetailsScreen.disabled_continue_button, True)
