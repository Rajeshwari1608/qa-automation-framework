import os

import pytest
from selenium import webdriver

from utils.db_connection import DatabaseConnection


@pytest.fixture
def driver():
    driver = webdriver.Chrome()

    driver.maximize_window()
    driver.delete_all_cookies()

    yield driver

    driver.quit()


@pytest.fixture
def database():
    db = DatabaseConnection()
    db.connect()

    db.execute_update("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL
        )
    """)

    db.execute_update("DELETE FROM users")

    yield db

    db.execute_update("DELETE FROM users")
    db.close()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):

    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:

        driver = item.funcargs.get("driver")

        if driver:
            os.makedirs("screenshots", exist_ok=True)

            screenshot_name = (
                item.nodeid
                .replace("/", "_")
                .replace("\\", "_")
                .replace("::", "_")
                .replace("[", "_")
                .replace("]", "_")
            )

            screenshot_path = os.path.join(
                "screenshots",
                f"{screenshot_name}.png"
            )

            driver.save_screenshot(screenshot_path)

            print(
                f"\nScreenshot saved: {screenshot_path}"
            )

