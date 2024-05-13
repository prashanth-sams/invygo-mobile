import time
from appium.webdriver.common.appiumby import AppiumBy
from src.helpers.app import App
from src.helpers.appiumdriver import Driver


class WeeklySubscriptionScreen(Driver):
    """
    weekly subscription listings screen locators
    """
    explore_all_cars = (AppiumBy.XPATH, '//button[contains(text(),"Explore all cars")]')
    filter_button = (AppiumBy.XPATH, "(//*/following-sibling::*//img[@loading='lazy'])[9]")
    sedan = (AppiumBy.XPATH, "//*[contains(text(),'Sedan')]/div")
    color = (AppiumBy.XPATH, "//*[contains(text(),'White')]/div")
    seats = (AppiumBy.XPATH, "//*[contains(text(),'5')]/div")
    show_cars = (AppiumBy.XPATH, "//button[contains(text(),'Show cars')]")
    select_car = (AppiumBy.XPATH, "(//div[@rows]//a[contains(@href,'/en-ae/dubai/weekly-subscription/rent')])[1]")
    
    
    def __init__(self, driver):
        super().__init__(driver)
    
    def filter_car(self):
        App.click(self, WeeklySubscriptionScreen.filter_button)
        App.click(self, WeeklySubscriptionScreen.sedan)
        App.click(self, WeeklySubscriptionScreen.color)
        App.click(self, WeeklySubscriptionScreen.seats)
        
        App.click(self, WeeklySubscriptionScreen.show_cars)
        App.click(self, WeeklySubscriptionScreen.select_car)