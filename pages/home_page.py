from selenium.webdriver.common.by import By

from pages.base_page import BasePage

signin_link = (By.ID, 'signin2')
login_link = (By.ID, 'login2')
cart_link = (By.ID, 'cartur')
signin_username_input = (By.ID, 'sign-username')
signin_password_input = (By.ID, 'sign-password')
signup_button = (By.XPATH, '//button[text()="Sign up"]')
all_product_titles = (By.CLASS_NAME, 'hrefch')
product_title = (By.XPATH, '//*[@class="hrefch" and text()="{}"]')
next_page_button = (By.ID, 'next2')


class HomePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def click_signin_button(self):
        self.click_on_element(*signin_link)

    def enter_username(self, text=''):
        self.element_enter_text(signin_username_input, text)

    def enter_password(self, text=''):
        self.element_enter_text(signin_password_input, text)

    def click_signup_button(self):
        self.click_on_element(*signup_button)

    def click_login_button(self):
        self.click_on_element(*login_link)

    def get_products_titles(self):
        products = self.driver.find_elements(*all_product_titles)
        return self.get_elements_text(products)

    def select_product(self, product_name=''):
        page_product_titles = self.get_products_titles()
        if product_name in page_product_titles:
            by_option, locator = product_title
            self.click_on_element(by_option, locator.format(product_name))
        else:
            if self.is_element_present(*next_page_button):
                self.click_on_element(*next_page_button)
                by_option, locator = product_title
                self.click_on_element(by_option, locator.format(product_name))
            else:
                raise ValueError(f'Product with name {product_name} was not found')

    def open_cart(self):
        self.click_on_element(*cart_link)
