from selenium.webdriver.common.by import By

from pages.base_page import BasePage


products_titles = (By.XPATH, '//table//tr[@class="success"]/td[2]')
total_price = (By.ID, 'totalp')
place_order_button = (By.XPATH, '//button[text()="Place Order"]')


class CartPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def get_products_titles(self):
        elements = self.driver.find_elements(*products_titles)
        return self.get_elements_text(elements)

    def get_total_price(self):
        return self.driver.find_element(*total_price).text

    def place_order(self):
        self.click_on_element(*place_order_button)
