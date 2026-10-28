import logging
from logger_config import setup_logging

import pytest
import os
import base64
from pytest_html import extras
from pages.checkout_overview_page import CheckoutOverviewPage
from pages.login_page import LoginPage
from pages.products_page import ProductsPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage

@pytest.fixture
def products_page(page):
    login_page = LoginPage()
    login_page.login(
        page,
        login_page.valid_username,
        login_page.valid_password
    )
    return page

@pytest.fixture
def cart_page(products_page):

    page = products_page

    # Product cart mein add karna
    products = ProductsPage()
    products.add_to_cart(page, "Sauce Labs Backpack")

    # Cart page open karna
    products.open_cart(page)

    return page

@pytest.fixture
def checkout_page(cart_page):
    page = cart_page

    # Checkout button per click karna
    cart = CartPage()
    cart.click_checkout_button(page)

    return page

@pytest.fixture
def checkout_overview_page(checkout_page):
    page = checkout_page

    # Customer ki details fill karna
    checkout = CheckoutPage()
    checkout.enter_checkout_information(
        page,
        "dildar_rana",
        "Choudhary",
        "250401"
    )
    checkout.click_continue_button(page)

    return page

@pytest.fixture
def checkout_complete_page(checkout_overview_page):

    page = checkout_overview_page

    # checkoutOverViewPage ka object banao
    overview_page = CheckoutOverviewPage()

    # Finish button click karna
    overview_page.click_finish_button(page)

    return page

# Take Screenshot on Test Failure and also add screenshot in report if test fail.
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.failed and report.when in ("setup", "call"):

        page = item.funcargs.get("page")

        if page is None:
            for fixture_value in item.funcargs.values():
                if hasattr(fixture_value, "screenshot"):
                    page = fixture_value
                    break

        if page is not None:
            os.makedirs("screenshots", exist_ok=True)

            screenshot_path = os.path.abspath(
                os.path.join("screenshots", f"{item.name}.png")
            )

            try:
                page.screenshot(
                    path=screenshot_path,
                    full_page=True
                )

                print(f"\nFailure screenshot saved: {screenshot_path}")

                # Attach screenshot to HTML report
                with open(screenshot_path, "rb") as image_file:
                    screenshot_base64 = base64.b64encode(
                        image_file.read()
                    ).decode("utf-8")

                report_extras = getattr(report, "extras", [])
                report_extras.append(
                    extras.image(screenshot_base64, mime_type="image/png")
                )
                report.extras = report_extras

            except Exception as error:
                print(f"\nScreenshot could not be saved: {error}")

# Logger_config function -------------------------------------------------------
# Test start hone par automatic log
def pytest_configure(config):
    worker_id = getattr(config, "workerinput", {}).get(
        "workerid", "main"
    )

    setup_logging(worker_id)


def pytest_runtest_logstart(nodeid, location):
    logger = logging.getLogger("automation")
    logger.info("TEST STARTED: %s", nodeid)


def pytest_runtest_logreport(report):
    logger = logging.getLogger("automation")

    if report.when == "setup" and report.failed:
        logger.error(
            "TEST FAILED DURING SETUP: %s\n%s",
            report.nodeid,
            report.longrepr
        )

    elif report.when == "call":
        if report.passed:
            logger.info(
                "TEST PASSED: %s | Duration: %.2f seconds",
                report.nodeid,
                report.duration
            )

        elif report.failed:
            logger.error(
                "TEST FAILED: %s | Duration: %.2f seconds\n%s",
                report.nodeid,
                report.duration,
                report.longrepr
            )

        elif report.skipped:
            logger.warning(
                "TEST SKIPPED: %s",
                report.nodeid
            )