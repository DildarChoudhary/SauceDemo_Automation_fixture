from playwright.sync_api import expect
from pages.login_page import LoginPage
from pages.products_page import ProductsPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from pages.checkout_overview_page import CheckoutOverviewPage


def test_checkout_overview_details(checkout_overview_page):

    page = checkout_overview_page


    # Checkout Overview page ka object banana
    overview_page = CheckoutOverviewPage()

    # Page title verify karna
    #assert overview_page.get_page_title(page) == "Checkout: Overview"
    expect(page.locator(".title")).to_have_text("Checkout: Overview")

    # Product name verify karna
    product_names = overview_page.get_product_names(page)
    assert "Sauce Labs Backpack" in product_names
    assert len(product_names) == 1

    # Product price verify karna
    product_prices = overview_page.get_product_prices(page)
    assert "$29.99" in product_prices

    # Subtotal verify karna
    subtotal = overview_page.get_subtotal(page)
    assert subtotal == "Item total: $29.99"

    # Tax verify karna
    tax = overview_page.get_tax(page)
    assert tax == "Tax: $2.40"

    # Final total verify karna
    total = overview_page.get_total(page)
    assert total == "Total: $32.39"

    # Data terminal mein print karna
    print("Product Names:", product_names)
    print("Product Prices:", product_prices)
    print("Subtotal:", subtotal)
    print("Tax:", tax)
    print("Total:", total)

    # Finish button click karna
    overview_page.click_finish_button(page)

    # Order confirmation verify karna
    assert page.locator(".complete-header").inner_text() == "Thank you for your order!"

# Cancel button per click karna oe wapas products page per navigate karna
def test_cancel_checkout_overview(checkout_overview_page):

    page = checkout_overview_page

    # CheckoutOverviewPage ka object banao
    checkout_overview_page = CheckoutOverviewPage()

    # Cancel button per click karna
    checkout_overview_page.click_cancel_button(page)

    page.wait_for_timeout(6000)

    # Verify karna ki user products page per wapas aagaya
    #assert page.locator(".title").inner_text() == "Products"
    expect(page.locator(".title")).to_have_text("Products")

    print(" Cancel Checkout Overview Test passed")