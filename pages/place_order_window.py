from time import sleep
from selenium.webdriver.common.by import By

from pages.base_page import BasePage


total_price = (By.ID, 'totalm')


class PlaceOrderWindow(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def get_total_price(self):
        text = self.driver.find_element(*total_price).text
        if not text:
            sleep(1)
            text = self.driver.find_element(*total_price).text
        return text.removeprefix('Total: ')
