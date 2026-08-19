from pages.login_page import LoginPage
from pages.products_page import ProductsPage


def test_products_page_is_displayed(driver):

    login_page = LoginPage(driver)
    products_page = ProductsPage(driver)

    login_page.open()
    login_page.login("standard_user", "secret_sauce")

    assert products_page.get_page_title() == "Products"


def test_products_are_available(driver):

    login_page = LoginPage(driver)
    products_page = ProductsPage(driver)

    login_page.open()
    login_page.login("standard_user", "secret_sauce")

    products = products_page.get_product_names()

    assert len(products) > 0
    assert "Sauce Labs Backpack" in products


def test_add_product_to_cart(driver):

    login_page = LoginPage(driver)
    products_page = ProductsPage(driver)

    login_page.open()
    login_page.login("standard_user", "secret_sauce")

    products_page.add_backpack_to_cart()

    assert products_page.get_cart_count() == "1"