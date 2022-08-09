import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


def get_driver():
    return webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))


@pytest.fixture(scope='session')
def driver():
    driver = get_driver()
    driver.implicitly_wait(5)
    driver.maximize_window()
    yield driver
    driver.quit()
