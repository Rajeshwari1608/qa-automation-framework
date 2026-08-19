from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ProductsPage:

    PAGE_TITLE = (By.CLASS_NAME, "title")
    PRODUCT_NAMES = (By.CLASS_NAME, "inventory_item_name")
    ADD_BACKPACK_BUTTON = (By.ID, "add-to-cart-sauce-labs-backpack")
    CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")
    CART_LINK = (By.CLASS_NAME, "shopping_cart_link")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def get_page_title(self):
        element = self.wait.until(
            EC.visibility_of_element_located(self.PAGE_TITLE)
        )
        return element.text

    def get_product_names(self):
        elements = self.wait.until(
            EC.presence_of_all_elements_located(self.PRODUCT_NAMES)
        )
        return [element.text for element in elements]

    def add_backpack_to_cart(self):
        button = self.wait.until(
            EC.element_to_be_clickable(self.ADD_BACKPACK_BUTTON)
        )
        button.click()

    def get_cart_count(self):
        badge = self.wait.until(
            EC.visibility_of_element_located(self.CART_BADGE)
        )
        return badge.text

    def open_cart(self):
        cart = self.wait.until(
            EC.element_to_be_clickable(self.CART_LINK)
        )
        cart.click()