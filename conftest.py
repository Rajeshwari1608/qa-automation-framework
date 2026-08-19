import os
import time

import pytest
from selenium import webdriver

from utils.db_connection import DatabaseConnection
from utils.logger import get_logger


logger = get_logger()


@pytest.fixture
def driver():
    logger.info("Starting browser")

    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.delete_all_cookies()

    yield driver

    logger.info("Closing browser")
    driver.quit()


@pytest.fixture
def database():
    logger.info("Starting database fixture")

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

    logger.info("Database fixture closed")


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):

    outcome = yield
    report = outcome.get_result()

    if report.when != "call":
        return

    duration = getattr(item, "_test_duration", 0)

    if report.passed:
        logger.info(
            f"TEST PASSED: {item.nodeid} | "
            f"Duration: {duration:.2f}s"
        )

    elif report.failed:
        logger.error(
            f"TEST FAILED: {item.nodeid} | "
            f"Duration: {duration:.2f}s"
        )

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

            logger.error(
                f"Screenshot saved: {screenshot_path}"
            )


@pytest.hookimpl(tryfirst=True)
def pytest_runtest_setup(item):
    item._test_start_time = time.time()


@pytest.hookimpl(trylast=True)
def pytest_runtest_call(item):
    item._test_duration = (
        time.time() - item._test_start_time
    )