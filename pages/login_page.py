from selenium.webdriver.common.by import By

from data.constants import USER_NAME, USER_PASSWORD
from pages.base_page import BasePage

login_username_input = (By.ID, 'loginusername')
login_password_input = (By.ID, 'loginpassword')
login_button = (By.XPATH, '//button[text()="Log in"]')


class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def enter_user_name_login(self, user_name=USER_NAME):
        self.element_enter_text(login_username_input, user_name)

    def enter_user_password_login(self, user_password=USER_PASSWORD):
        self.element_enter_text(login_password_input, user_password)

    def click_login_button_form(self):
        self.click_on_element(*login_button)
