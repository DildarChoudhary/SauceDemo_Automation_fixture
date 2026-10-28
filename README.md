# SauceDemo Automation Framework

## Project Overview
This project automates SauceDemo web application testing using Python, Playwright, and Pytest.

## Technologies Used
- Python
- Playwright
- Pytest
- Pytest-xdist
- Pytest-html
- Page Object Model (POM)

## Project Structure
- Tests/        - Test cases
- pages/        - Page Object Model classes
- reports/      - HTML test reports
- screenshots/  - Failure screenshots
- test-results/ - Playwright test artifacts
- conftest.py   - Shared fixtures and hooks
- pytest.ini    - Pytest configuration
- requirements.txt - Project dependencies

## Installation
Install project dependencies:

```powershell
python -m pip install -r requirements.txt
```

Install Playwright browsers:

```powershell
python -m playwright install
```

## Run Tests

Run all tests:

```powershell
python -m pytest
```

Run tests on Chromium:

```powershell
python -m pytest --browser chromium
```

Run tests on Firefox:

```powershell
python -m pytest --browser firefox
```

Run tests on WebKit:

```powershell
python -m pytest --browser webkit
```

Run tests on all three browsers:

```powershell
python -m pytest --browser chromium --browser firefox --browser webkit
```

## Parallel Execution

Run tests using four workers:

```powershell
python -m pytest -n 4
```

## HTML Report

Generate a self-contained HTML report:

```powershell
python -m pytest --html=reports/report.html --self-contained-html
```

Open `reports/report.html` in a browser to view the results.

Automation Framework: Python + Playwright + Pytest