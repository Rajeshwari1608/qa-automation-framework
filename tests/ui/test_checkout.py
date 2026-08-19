from pages.login_page import LoginPage
from pages.products_page import ProductsPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage


def test_successful_checkout(driver):

    login_page = LoginPage(driver)
    products_page = ProductsPage(driver)
    cart_page = CartPage(driver)
    checkout_page = CheckoutPage(driver)

    login_page.open()
    login_page.login("standard_user", "secret_sauce")

    products_page.add_backpack_to_cart()
    products_page.open_cart()

    cart_page.checkout()

    checkout_page.enter_first_name("Rajeshwari")
    checkout_page.enter_last_name("Test")
    checkout_page.enter_postal_code("560001")

    checkout_page.continue_checkout()
    checkout_page.finish_order()

    assert checkout_page.get_confirmation_message() == "Thank you for your order!"