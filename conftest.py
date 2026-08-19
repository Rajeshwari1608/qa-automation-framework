import pytest
import logging

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from utils.db_connection import DatabaseConnection


# ---------------------------------------
# Logging
# ---------------------------------------

logging.basicConfig(
    filename="logs/test_execution.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logger = logging.getLogger("qa_framework")


# ---------------------------------------
# Browser fixture
# ---------------------------------------

@pytest.fixture
def driver():

    logger.info("Starting browser")

    options = Options()

    # Disable Chrome password manager
    options.add_experimental_option(
        "prefs",
        {
            "credentials_enable_service": False,
            "profile.password_manager_enabled": False,
            "profile.password_manager_leak_detection": False,
            "autofill.profile_enabled": False,
            "autofill.credit_card_enabled": False
        }
    )

    options.add_argument(
        "--disable-save-password-bubble"
    )

    options.add_argument(
        "--disable-features=PasswordLeakDetection"
    )

    driver = webdriver.Chrome(options=options)

    driver.maximize_window()

    driver.implicitly_wait(2)

    yield driver

    logger.info("Closing browser")

    driver.quit()


# ---------------------------------------
# Database fixture
# ---------------------------------------

@pytest.fixture
def database():

    db = DatabaseConnection("test_database.db")

    yield db

    db.close()