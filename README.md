# E-Commerce UI Automation Framework

A Selenium and Pytest-based UI automation framework designed for scalable end-to-end web testing using the Page Object Model (POM) architecture.

## Overview

This project automates a complete e-commerce workflow including:

- Login validation
- Product verification
- Add-to-cart functionality
- Checkout process
- Failure screenshot capture
- HTML report generation

The framework demonstrates scalable automation design principles focused on maintainability, reusability, and clean project structure.

---

## Features

### UI Automation

- Automated browser launch and teardown
- Login validation with valid and invalid credentials
- Product page verification
- Add-to-cart functionality
- End-to-end checkout workflow automation

### Reporting

- HTML report generation using `pytest-html`
- Failure screenshot capture with timestamp-based naming
- Independent test execution with fresh browser sessions

### Framework Design

- Page Object Model (POM) architecture
- Centralized WebDriver management
- Reusable explicit wait utilities
- Modular project structure

---

## Tech Stack

- Python
- Selenium WebDriver
- Pytest
- WebDriver Manager
- pytest-html
- Page Object Model (POM)

---

## Project Structure

```bash
ecommerce-ui-automation-framework/
│
├── pages/              # Page Object classes
├── tests/              # Test cases
├── utils/              # Driver factory & wait utilities
├── screenshots/        # Failure screenshots
├── reports/            # HTML execution reports
├── conftest.py         # Pytest fixtures & hooks
├── requirements.txt    # Dependencies
└── README.md
```

---

## Installation

### Clone Repository

```bash
git clone https://github.com/pavan123chinta/ecommerce-ui-automation-framework.git
cd ecommerce-ui-automation-framework
```

### Create Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Run Tests

### Execute Test Suite

```bash
pytest
```

### Generate HTML Report

```bash
pytest -v --html=reports/report.html --self-contained-html
```

---

## Sample Test Scenarios

- Validate successful login
- Validate error message for invalid login
- Verify products page loads after login
- Verify cart badge updates after adding product
- Complete end-to-end checkout flow

---

## Screenshot Handling

Failure screenshots are captured using the `pytest_runtest_makereport` hook implemented in `conftest.py`.

Screenshots are automatically stored inside:

```bash
screenshots/
```

---

## Reporting

HTML reports are generated inside:

```bash
reports/
```

Each test execution creates a detailed report for easier debugging and execution tracking.

---

## Key Concepts Demonstrated

- UI automation testing
- Selenium WebDriver integration
- Page Object Model implementation
- Test scalability and reusability
- Failure screenshot handling
- Automated HTML reporting
- Modular framework architecture

---

## Author

**Pavan Chinta**  
QA Automation Engineer | Selenium | Pytest | Python
