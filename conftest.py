import pytest
from selenium import webdriver

from utils.db_connection import DatabaseConnection


@pytest.fixture
def driver():
    driver = webdriver.Chrome()

    driver.maximize_window()

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

    # Clean existing data before every test
    db.execute_update("DELETE FROM users")

    yield db

    # Clean data after every test
    db.execute_update("DELETE FROM users")
    db.close()