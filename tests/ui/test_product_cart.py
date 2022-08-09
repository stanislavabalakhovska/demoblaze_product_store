from data.constants import USER_NAME, USER_PASSWORD, HOME_PAGE_URL
from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.product_page import ProductPage
from pages.cart_page import CartPage
from pages.place_order_window import PlaceOrderWindow


def create_user(driver):
    home_page = HomePage(driver)
    home_page.click_signin_button()
    home_page.enter_username(USER_NAME)
    home_page.enter_password(USER_PASSWORD)
    home_page.click_signup_button()
    home_page.dismiss_alert()


def login_user(driver):
    home_page = HomePage(driver)
    home_page.click_login_button()
    login_page = LoginPage(driver)
    login_page.enter_user_name_login()
    login_page.enter_user_password_login()
    login_page.click_login_button_form()


def test_order_price(driver):
    driver.get(HOME_PAGE_URL)
    create_user(driver)
    login_user(driver)
    home_page = HomePage(driver)
    home_page.select_product('Nexus 6')
    product_page = ProductPage(driver)
    product_page.click_add_to_cart()
    driver.back()
    home_page = HomePage(driver)
    home_page.select_product('MacBook Pro')
    product_page = ProductPage(driver)
    product_page.click_add_to_cart()
    driver.back()
    home_page.open_cart()
    cart_page = CartPage(driver)
    assert 'Nexus 6' in cart_page.get_products_titles(), 'Nexus 6 was not added to cart'
    assert 'MacBook Pro' in cart_page.get_products_titles(), 'MacBook Pro was not added to cart'
    expected_price = '1750'
    assert cart_page.get_total_price() == expected_price
    cart_page.place_order()
    window = PlaceOrderWindow(driver)
    assert window.get_total_price() == expected_price
