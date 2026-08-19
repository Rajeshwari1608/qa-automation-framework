from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CartPage:

    CART_ITEMS = (By.CLASS_NAME, "cart_item")
    PRODUCT_NAMES = (By.CLASS_NAME, "inventory_item_name")
    REMOVE_BACKPACK = (By.ID, "remove-sauce-labs-backpack")
    CHECKOUT_BUTTON = (By.ID, "checkout")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def get_cart_items(self):
        return self.driver.find_elements(*self.CART_ITEMS)

    def get_product_names(self):
        items = self.wait.until(
            EC.presence_of_all_elements_located(self.PRODUCT_NAMES)
        )
        return [item.text for item in items]

    def remove_backpack(self):
        button = self.wait.until(
            EC.element_to_be_clickable(self.REMOVE_BACKPACK)
        )
        button.click()

    def checkout(self):
        button = self.wait.until(
            EC.element_to_be_clickable(self.CHECKOUT_BUTTON)
        )
        button.click()