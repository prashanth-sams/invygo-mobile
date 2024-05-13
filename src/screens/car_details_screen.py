from appium.webdriver.common.appiumby import AppiumBy
from src.helpers.app import App
from src.helpers.appiumdriver import Driver


class CarDetailsScreen(Driver):
    """
    car details screen locators
    """
    contract_length = (AppiumBy.XPATH, "//h1[contains(text(),'Contract length')]")
    three_months = (AppiumBy.XPATH, "(//div[contains(text(),'3 months')]/parent::*/parent::div/div/div)[1]")
    subscribe_button = (AppiumBy.XPATH, "//button[contains(text(),'Subscribe')]")
    popup_header = (AppiumBy.XPATH, "//h1[contains(text(),'Let’s get started')]")
    disabled_continue_button = (AppiumBy.XPATH, "//button[@disabled][contains(text(),'Continue')]")
    
    
    def __init__(self, driver):
        super().__init__(driver)
    
    def subscribe(self):
        """
        This method does monthly subscription
        """
        App.click(self, CarDetailsScreen.three_months)
        App.click(self, CarDetailsScreen.subscribe_button)
        
        