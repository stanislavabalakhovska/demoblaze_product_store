from selenium.common import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def click_on_element(self, by_option, locator):
        self.driver.find_element(by_option, locator).click()

    def element_enter_text(self, element, text=''):
        """Enter specified text into text field

        Args:
            element: Text field where text is entered
            text: Text to enter
        """
        elem = self.wait.until(EC.presence_of_element_located(element))
        elem.clear()
        elem.send_keys(text)

    def dismiss_alert(self):
        self.wait.until(EC.alert_is_present())
        self.driver.switch_to.alert.accept()

    def is_element_present(self, by_option, locator):
        try:
            self.driver.find_element(by_option, locator)
        except NoSuchElementException:
            return False
        return True

    def get_elements_text(self, elements_list=[]):
        return [elem.text for elem in elements_list]
