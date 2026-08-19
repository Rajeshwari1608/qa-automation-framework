import json
import pytest

from pages.login_page import LoginPage


with open("test_data/login_data.json", "r") as file:
    LOGIN_DATA = json.load(file)


def test_valid_login(driver):

    login_page = LoginPage(driver)

    login_page.open()

    user = LOGIN_DATA["valid_user"]

    login_page.login(
        user["username"],
        user["password"]
    )

    assert "inventory.html" in driver.current_url


@pytest.mark.parametrize(
    "username,password",
    [
        (
            LOGIN_DATA["invalid_user"]["username"],
            LOGIN_DATA["invalid_user"]["password"]
        ),
        (
            LOGIN_DATA["locked_user"]["username"],
            LOGIN_DATA["locked_user"]["password"]
        )
    ]
)
def test_invalid_login(driver, username, password):

    login_page = LoginPage(driver)

    login_page.open()

    login_page.login(username, password)

    assert "inventory.html" not in driver.current_url