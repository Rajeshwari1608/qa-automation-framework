from pages.login_page import LoginPage
from pages.products_page import ProductsPage
from pages.cart_page import CartPage


def test_product_is_present_in_cart(driver):

    login_page = LoginPage(driver)
    products_page = ProductsPage(driver)
    cart_page = CartPage(driver)

    login_page.open()
    login_page.login("standard_user", "secret_sauce")

    products_page.add_backpack_to_cart()
    products_page.open_cart()

    products = cart_page.get_product_names()

    assert "Sauce Labs Backpack" in products


def test_remove_product_from_cart(driver):

    login_page = LoginPage(driver)
    products_page = ProductsPage(driver)
    cart_page = CartPage(driver)

    login_page.open()
    login_page.login("standard_user", "secret_sauce")

    products_page.add_backpack_to_cart()
    products_page.open_cart()

    cart_page.remove_backpack()

    assert len(cart_page.get_cart_items()) == 0