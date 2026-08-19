from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CheckoutPage:

    FIRST_NAME = (By.ID, "first-name")
    LAST_NAME = (By.ID, "last-name")
    POSTAL_CODE = (By.ID, "postal-code")

    CONTINUE_BUTTON = (By.ID, "continue")
    FINISH_BUTTON = (By.ID, "finish")

    PAGE_TITLE = (By.CLASS_NAME, "title")

    ORDER_CONFIRMATION = (
        By.CLASS_NAME,
        "complete-header"
    )

    ERROR_MESSAGE = (
        By.CSS_SELECTOR,
        "h3[data-test='error']"
    )

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)

    def enter_first_name(self, first_name):
        self._set_field(self.FIRST_NAME, first_name)

    def enter_last_name(self, last_name):
        self._set_field(self.LAST_NAME, last_name)

    def enter_postal_code(self, postal_code):
        self._set_field(self.POSTAL_CODE, postal_code)

    def _set_field(self, locator, value):

        value = str(value)

        element = self.wait.until(
            EC.presence_of_element_located(locator)
        )

        self.driver.execute_script(
            """
            const element = arguments[0];
            const value = arguments[1];

            element.focus();

            const setter =
                Object.getOwnPropertyDescriptor(
                    HTMLInputElement.prototype,
                    'value'
                ).set;

            setter.call(element, value);

            element.dispatchEvent(
                new Event('input', { bubbles: true })
            );

            element.dispatchEvent(
                new Event('change', { bubbles: true })
            );

            element.blur();
            """,
            element,
            value
        )

        actual_value = self.driver.find_element(
            *locator
        ).get_attribute("value")

        assert actual_value == value, (
            f"Expected '{value}' but got '{actual_value}' "
            f"for {locator}"
        )

    def continue_checkout(self):

        first_name = self.driver.find_element(
            *self.FIRST_NAME
        ).get_attribute("value")

        last_name = self.driver.find_element(
            *self.LAST_NAME
        ).get_attribute("value")

        postal_code = self.driver.find_element(
            *self.POSTAL_CODE
        ).get_attribute("value")

        print("\nCheckout values:")
        print("First name:", repr(first_name))
        print("Last name:", repr(last_name))
        print("Postal code:", repr(postal_code))

        assert first_name == "Rajeshwari"
        assert last_name == "Test"
        assert postal_code == "560001"

        button = self.wait.until(
            EC.element_to_be_clickable(
                self.CONTINUE_BUTTON
            )
        )

        button.click()

        self.wait.until(
            EC.url_contains(
                "checkout-step-two.html"
            )
        )

    def verify_checkout_overview(self):

        title = self.wait.until(
            EC.visibility_of_element_located(
                self.PAGE_TITLE
            )
        )

        return title.text

    def finish_order(self):

        button = self.wait.until(
            EC.element_to_be_clickable(
                self.FINISH_BUTTON
            )
        )

        button.click()

        self.wait.until(
            EC.url_contains(
                "checkout-complete.html"
            )
        )

    def get_confirmation_message(self):

        return self.wait.until(
            EC.visibility_of_element_located(
                self.ORDER_CONFIRMATION
            )
        ).text

    def get_error_message(self):

        return self.wait.until(
            EC.visibility_of_element_located(
                self.ERROR_MESSAGE
            )
        ).text