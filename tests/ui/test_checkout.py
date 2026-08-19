import json

from pages.login_page import LoginPage
from pages.products_page import ProductsPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage


with open("test_data/checkout_data.json", "r") as file:
    CHECKOUT_DATA = json.load(file)


def test_successful_checkout(driver):

    login_page = LoginPage(driver)
    products_page = ProductsPage(driver)
    cart_page = CartPage(driver)
    checkout_page = CheckoutPage(driver)

    # Login
    login_page.open()

    login_page.login(
        "standard_user",
        "secret_sauce"
    )

    # Add product
    products_page.add_backpack_to_cart()
    products_page.open_cart()

    # Open checkout
    cart_page.checkout()

    # Customer information
    customer = CHECKOUT_DATA["valid_customer"]

    checkout_page.enter_first_name(
        customer["first_name"]
    )

    checkout_page.enter_last_name(
        customer["last_name"]
    )

    checkout_page.enter_postal_code(
        customer["postal_code"]
    )

    # Continue to overview
    checkout_page.continue_checkout()

    # Verify overview page
    assert checkout_page.verify_checkout_overview() == "Checkout: Overview"

    # Finish order
    checkout_page.finish_order()

    # Verify successful order
    assert checkout_page.get_confirmation_message() == "Thank you for your order!"