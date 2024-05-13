from appium.webdriver.common.appiumby import AppiumBy
from src.helpers.appiumdriver import Driver


class CarSpecsScreen(Driver):
    """
    specs screen locators
    """
    all_cars = (AppiumBy.XPATH, '//*[contains(text(), "Learn More")]')
    monthly_plans = (AppiumBy.CSS_SELECTOR, '[title="Monthly plans"]')
    specs_bg = (AppiumBy.CSS_SELECTOR, '[alt="explore cars"]')
    
    
    def __init__(self, driver):
        super().__init__(driver)
    