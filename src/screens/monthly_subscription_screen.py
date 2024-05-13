import time
from appium.webdriver.common.appiumby import AppiumBy
from src.helpers.app import App
from src.helpers.appiumdriver import Driver


class MonthlySubscriptionScreen(Driver):
    """
    monthly subscription listings screen locators
    """
    explore_all_cars = (AppiumBy.XPATH, '//button[contains(text(),"Explore all cars")]')
    filter_button = (AppiumBy.XPATH, "(//*[@direction='column']/following-sibling::*//img[@loading='lazy'])[2]")
    sedan = (AppiumBy.XPATH, "//*[contains(text(),'Sedan')]/div")
    color = (AppiumBy.XPATH, "//*[contains(text(),'White')]/div")
    seats = (AppiumBy.XPATH, "//*[contains(text(),'5')]/div")
    show_cars = (AppiumBy.XPATH, "//button[contains(text(),'Show cars')]")
    select_car = (AppiumBy.XPATH, "(//div[@rows]//a[contains(@href,'/en-ae/dubai/monthly-subscription/rent')])[1]")
    
    
    def __init__(self, driver):
        super().__init__(driver)
    
    def filter_car(self):
        App.click(self, MonthlySubscriptionScreen.filter_button)
        App.click(self, MonthlySubscriptionScreen.sedan)
        App.click(self, MonthlySubscriptionScreen.color)
        App.click(self, MonthlySubscriptionScreen.seats)
        
        App.click(self, MonthlySubscriptionScreen.show_cars)
        App.click(self, MonthlySubscriptionScreen.select_car)