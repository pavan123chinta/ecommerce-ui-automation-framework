E-Commerce UI Automation Framework
Project Overview

This project is a Selenium + Pytest based UI Automation Framework built using Python and designed using the Page Object Model (POM) architecture.

The framework automates an end-to-end E-Commerce flow including:

Login validation

Product verification

Add to cart functionality

Checkout process

Failure screenshot capture

HTML report generation

It demonstrates real-world automation framework design principles focusing on scalability, maintainability, and clean structure.

Tech Stack

Python

Selenium WebDriver

Pytest

WebDriver Manager

pytest-html

Page Object Model (POM)

Framework Architecture
ecommerce-ui-automation-framework/
│
├── pages/              # Page Object classes
├── tests/              # Test cases
├── utils/              # Driver factory & waits
├── screenshots/        # Failure screenshots
├── reports/            # HTML execution reports
├── conftest.py         # Pytest fixtures & hooks
├── requirements.txt    # Dependencies
└── README.md

Key Design Principles

Page Object Model for separation of concerns

Centralized WebDriver management

Reusable explicit wait utilities

Independent test cases

Automatic failure screenshot capture

Self-contained HTML execution report

Features Implemented

✔ Automated browser launch & teardown
✔ Login with valid and invalid credentials
✔ Product page validation
✔ Add to cart verification
✔ Complete checkout flow automation
✔ Screenshot capture on test failure
✔ HTML report generation using pytest-html

Sample Test Scenarios

Validate successful login

Validate error message on invalid login

Verify products page loads after login

Verify cart badge updates after adding product

Complete end-to-end checkout flow

How to Run the Project
1️ Clone the repository
git clone https://github.com/pavan123chinta/ecommerce-ui-automation-framework.git
cd ecommerce-ui-automation-framework

2️ Create virtual environment
python -m venv venv
venv\Scripts\activate

3️ Install dependencies
pip install -r requirements.txt

4️ Execute tests with HTML report
pytest -v --html=reports/report.html --self-contained-html

Reporting

HTML report is generated inside /reports

Screenshots are automatically saved inside /screenshots on failure

Each test runs independently with a fresh browser session

Screenshot Handling

Failure screenshots are captured using the pytest_runtest_makereport hook implemented in conftest.py.

This ensures automatic capture on failure with timestamp-based naming for easier debugging.

Author

Pavan Chinta
QA Automation Engineer | Selenium | Pytest | Python
