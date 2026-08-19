# QA Automation Framework


A Python-based QA automation framework for testing web applications, REST APIs, and databases using Selenium, Pytest, Requests, and SQLite.


The framework is designed using reusable components and follows automation best practices such as the Page Object Model, external test data, reusable fixtures, logging, screenshots, and HTML reporting.


---


## 📌 Project Overview


This project provides automated testing across three major layers:


- **UI Testing** using Selenium WebDriver
- **API Testing** using Requests
- **Database Testing** using SQLite


The framework uses **Pytest** as the test execution and reporting foundation.


### Key Features


- Selenium WebDriver automation
- Page Object Model (POM)
- Pytest test framework
- REST API automation
- SQLite database testing
- External JSON test data
- Reusable Pytest fixtures
- Explicit waits for UI synchronization
- Logging
- Failure screenshots
- HTML test reports
- Configurable test execution
- Git version control


---


# 🛠️ Technology Stack


| Technology | Purpose |
|---|---|
| Python | Programming language |
| Pytest | Test automation framework |
| Selenium WebDriver | Web UI automation |
| Requests | REST API testing |
| SQLite | Database testing |
| pytest-html | HTML test reporting |
| JSON | External test data |
| python-dotenv | Configuration management |
| Git | Version control |
| Chrome WebDriver | Browser automation |


---


# 📁 Project Structure


```text
qa-automation-framework/
│
├── pages/
│   ├── login_page.py
│   ├── products_page.py
│   ├── cart_page.py
│   └── checkout_page.py
│
├── tests/
│   │
│   ├── ui/
│   │   ├── test_login.py
│   │   ├── test_products.py
│   │   ├── test_cart.py
│   │   └── test_checkout.py
│   │
│   ├── api/
│   │   └── test_users_api.py
│   │
│   └── database/
│       └── test_database.py
│
├── test_data/
│   └── checkout_data.json
│
├── utils/
│   ├── config.py
│   ├── db_connection.py
│   └── logger.py
│
├── logs/
│   └── test_execution.log
│
├── reports/
│   └── test_report.html
│
├── screenshots/
│   └── UI failure screenshots
│
├── conftest.py
├── requirements.txt
├── pytest.ini
├── .gitignore
├── README.md
└── test_database.db
🧪 Testing Scope
1. UI Automation

The UI automation layer uses Selenium WebDriver and follows the Page Object Model.

The application under test is:

https://www.saucedemo.com
UI Test Coverage

The framework currently covers:

Login Testing
Valid user login
Invalid username/password
Locked-out user login
Product Testing
Products page verification
Product availability
Adding a product to cart
Cart Testing
Verify product is present in cart
Remove product from cart
Checkout Testing
Enter customer information
Navigate to checkout overview
Complete checkout
Verify successful order confirmation
Current UI Test Count
9 UI tests
🌐 API Automation

The API automation layer uses the Python requests library.

API Test Coverage

The framework currently covers:

Get all users
Get a single user
Create a user
Update a user
Delete a user
Invalid user request
Invalid endpoint
Response structure validation
API response time validation
Response schema validation
Current API Test Count
10 API tests
🗄️ Database Automation

Database testing is implemented using SQLite.

The database layer contains a reusable database connection class responsible for:

Opening database connections
Executing SELECT queries
Executing INSERT/UPDATE/DELETE queries
Committing database changes
Closing connections
Database Test Coverage

The framework currently covers:

Insert and read user
Update user
Delete user
Current Database Test Count
3 database tests
🏗️ Framework Architecture

The framework follows a layered architecture.

                    QA AUTOMATION FRAMEWORK
                             │
             ┌───────────────┼───────────────┐
             │               │               │
             ▼               ▼               ▼
        UI Testing       API Testing     DB Testing
             │               │               │
             ▼               ▼               ▼
        Page Objects      Requests        SQLite
             │               │               │
             └───────────────┼───────────────┘
                             │
                             ▼
                         Pytest
                             │
                  ┌──────────┼──────────┐
                  ▼          ▼          ▼
                Logs     Screenshots   Reports
🧱 Page Object Model

The UI automation follows the Page Object Model (POM) design pattern.

Each application page has a dedicated Python class.

For example:

LoginPage
ProductsPage
CartPage
CheckoutPage

Each page object contains:

Page locators
Page actions
Explicit waits
Page-specific validation methods
Benefits

Using POM provides:

Better code organization
Improved maintainability
Reusable page actions
Reduced duplication
Easier debugging
Easier maintenance when UI elements change
📊 Test Data Management

Test data is separated from the test implementation.

Checkout data is stored in:

test_data/checkout_data.json

Example:

{
    "valid_customer": {
        "first_name": "Rajeshwari",
        "last_name": "Test",
        "postal_code": "560001"
    }
}

The test reads the data from the JSON file instead of hardcoding the values directly inside the test.

This makes it easier to:

Change test data
Add additional test scenarios
Reuse data
Maintain tests independently from test data
🔧 Configuration

Configuration-related values are maintained separately from test implementation.

The framework contains:

utils/config.py

This provides a central location for configuration values used by the framework.

Environment-specific configuration can be extended in the future using environment variables or .env files.

🔌 Database Connection

Database operations are handled through:

utils/db_connection.py

The DatabaseConnection class provides reusable methods for database interaction.

Example operations include:

execute_query()
execute_update()
connect()
close()

This prevents database connection logic from being duplicated across tests.

📝 Logging

The framework contains a reusable logging utility:

utils/logger.py

Execution logs are stored in:

logs/test_execution.log

Logging is also integrated with the Pytest framework.

Example log:

2026-08-19 23:35:50,045 - INFO - LOGGER TEST SUCCESS

Browser lifecycle events are also logged.

Example:

INFO - Starting browser
INFO - Closing browser

Logging helps with:

Debugging
Test execution tracking
Failure investigation
CI/CD troubleshooting
📸 Failure Screenshots

The framework supports screenshots for UI test failures.

Screenshots are stored in:

screenshots/

This provides visual information about the browser state when a Selenium test fails.

Screenshots can help identify:

Incorrect page state
Missing elements
Navigation problems
UI changes
Synchronization issues
📄 HTML Test Reports

The framework uses pytest-html to generate HTML test reports.

Run:

python -m pytest tests/ui tests/api tests/database -v --html=reports/test_report.html --self-contained-html

The generated report will be available at:

reports/test_report.html

The report provides information such as:

Test names
Test status
Execution duration
Failure information
Environment information
Captured logs
⚙️ Installation
1. Clone the Repository
git clone <your-github-repository-url>

Move into the project:

cd qa-automation-framework
2. Create Virtual Environment
python -m venv venv
3. Activate Virtual Environment

For Windows PowerShell:

.\venv\Scripts\Activate.ps1

You should see:

(venv)

at the beginning of the terminal prompt.

4. Install Dependencies
pip install -r requirements.txt
▶️ Running Tests
Run All UI Tests
python -m pytest tests/ui -v
Run All API Tests
python -m pytest tests/api -v
Run All Database Tests
python -m pytest tests/database -v
Run the Complete Test Suite
python -m pytest tests/ui tests/api tests/database -v
📊 Current Test Results

The current framework contains:

Test Layer	Tests
UI	9
API	10
Database	3
Total	22

Latest successful execution:

22 passed

Therefore:

UI Tests        → 9 passed
API Tests       → 10 passed
Database Tests  → 3 passed


Total           → 22 passed
🧪 Example Test Execution

Run:

python -m pytest tests/ui tests/api tests/database -v

Expected result:

======================= test session starts =======================


collected 22 items


... PASSED
... PASSED
... PASSED


======================= 22 passed =======================
🔍 Running Individual Tests

Run the login tests:

python -m pytest tests/ui/test_login.py -v

Run checkout:

python -m pytest tests/ui/test_checkout.py -v

Run API tests:

python -m pytest tests/api/test_users_api.py -v

Run database tests:

python -m pytest tests/database/test_database.py -v
🛠️ Debugging Tests

For more detailed output:

python -m pytest tests/ui/test_checkout.py -v -s

The -s option displays print statements during execution.

For example:

First name: 'Rajeshwari'
Last name: 'Test'
Postal code: '560001'
🧹 Project Cleanup

Temporary Pytest cache can be removed with:

Remove-Item -Recurse -Force .pytest_cache

Generated screenshots can be removed with:

Remove-Item .\screenshots\*.png

Generated reports can be removed when required:

Remove-Item .\reports\*.html
🔐 Security

Sensitive information such as:

API keys
Passwords
Access tokens
Environment-specific secrets

should not be committed to Git.

Use environment variables or .env files for sensitive configuration.

The .env file should be included in .gitignore.

📦 Dependencies

The main dependencies used by the framework are:

pytest
selenium
requests
pytest-html
pytest-metadata
webdriver-manager
python-dotenv
jsonschema

The complete dependency list is available in:

requirements.txt
🔄 Version Control

The project uses Git for version control.

Check repository status:

git status

Add changes:

git add .

Commit changes:

git commit -m "Update QA automation framework"

Push changes:

git push origin main
🚀 Future Improvements

The framework can be further enhanced with:

CI/CD

Integrate the framework with GitHub Actions to automatically execute tests whenever code is pushed.

Parallel Execution

Use Pytest parallel execution to reduce test execution time.

Example future command:

pytest -n 4
Test Markers

Introduce markers such as:

ui
api
database
smoke
regression

This would allow selective test execution.

Example:

pytest -m smoke
Environment Management

Support multiple environments such as:

Development
Testing
Staging
Production

using environment variables.

Enhanced API Testing

Additional API scenarios can include:

Authentication
Authorization
Headers
Query parameters
Negative scenarios
Boundary testing
Response payload validation
Enhanced Database Testing

Additional database scenarios can include:

Constraint validation
Duplicate records
Invalid data
Transaction rollback
Referential integrity
Data consistency
Enhanced UI Testing

Additional UI scenarios can include:

Logout
Product sorting
Multiple products
Checkout validation errors
Empty cart scenarios
Session handling
Navigation validation
📈 Future Framework Architecture

The planned framework can evolve toward:

                    GitHub Repository
                           │
                           ▼
                     GitHub Actions
                           │
                           ▼
                      Pytest Suite
                           │
          ┌────────────────┼────────────────┐
          ▼                ▼                ▼
       UI Tests         API Tests       DB Tests
          │                │                │
          ▼                ▼                ▼
      Selenium          Requests          SQLite
          │                │                │
          └────────────────┼────────────────┘
                           ▼
                    Test Results
                           │
             ┌─────────────┼─────────────┐
             ▼             ▼             ▼
          HTML Report    Logs       Screenshots
🎯 Project Objective

The objective of this project is to demonstrate the implementation of a maintainable QA automation framework capable of validating different layers of an application.

The framework demonstrates practical knowledge of:

Test automation
Selenium
Pytest
Page Object Model
API testing
Database testing
Test data management
Logging
Reporting
Debugging
Git
Automation framework design
👩‍💻 Author

Rajeshwari S

Computer Science Engineering
Artificial Intelligence and Data Engineering