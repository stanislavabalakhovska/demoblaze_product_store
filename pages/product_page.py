from selenium.webdriver.common.by import By

from pages.base_page import BasePage


add_to_cart_button = (By.XPATH, '//a[text()="Add to cart"]')


class ProductPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def click_add_to_cart(self):
        self.click_on_element(*add_to_cart_button)
        self.dismiss_alert()
        self.driver.back()
