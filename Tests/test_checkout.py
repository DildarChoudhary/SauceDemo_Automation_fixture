from playwright.sync_api import expect
from pages.login_page import LoginPage
from pages.products_page import ProductsPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage

# Test 1:Valid checkout iformation test karna
def test_checkout_information(checkout_page):

    page = checkout_page

    # CheckoutPage ka object banana
    checkout_page = CheckoutPage()

    # Customer ki details fill karna
    checkout_page.enter_checkout_information(
        page,
    "Dildar",
    "Choudhary",
  "250401"
    )

    # Continue button per click karna
    checkout_page.click_continue_button(page)

    # Checkout overview page ka title verify karna
    #assert page.locator(".title").inner_text() == "Checkout: Overview"
    expect(page.locator(".title")).to_have_text("Checkout: Overview")

    # Test result terminal mein print karana
    print("checkout information test passed")

# Test 2: All fields blank
def test_checkout_all_fields_blank(checkout_page):

    page = checkout_page

    # CheckoutPage ka object banao
    checkout_page = CheckoutPage()

    # Continue button per click karna
    checkout_page.click_continue_button(page)

    # Error msg lene
    error = checkout_page.get_error_message(page)

    # error msg Verify karna
    assert "First Name is required" in error

    print("All fields blank :", error)

# Test 3: First Name blank
def test_checkout_first_name_blank(checkout_page):

    page = checkout_page
    checkout_page = CheckoutPage()

    checkout_page.enter_checkout_information(
        page, "", "Rana", "201301"
    )

    checkout_page.click_continue_button(page)

    error = checkout_page.get_error_message(page)

    assert "First Name is required" in error

    print("First name blank :", error)


# Test 4: Last Name blank
def test_checkout_last_name_blank(checkout_page):

    page = checkout_page
    checkout_page = CheckoutPage()

    checkout_page.enter_checkout_information(
        page, "Dildar", "", "201301"
    )

    checkout_page.click_continue_button(page)

    error = checkout_page.get_error_message(page)

    assert "Last Name is required" in error

    print("Last name blank :", error)


# Test 5: Postal Code blank
def test_checkout_postal_code_blank(checkout_page):

    page = checkout_page
    checkout_page = CheckoutPage()

    checkout_page.enter_checkout_information(
        page, "Dildar", "Rana", ""
    )

    checkout_page.click_continue_button(page)

    error = checkout_page.get_error_message(page)

    assert "Postal Code is required" in error

    print("postal code blank :", error)

# Test 6: Cancel button per click karna or wapas cart page per aana
def test_cancel_checkout(checkout_page):

    page = checkout_page

    # Checkout class ka object banana
    checkout_page = CheckoutPage()

    # Cancel button per click karna
    checkout_page.click_cancel_button(page)

    # Verify karna ki user Cart page par wapas aa gaya
    #assert page.locator(".title").inner_text() == "Your Cart"
    expect(page.locator(".title")).to_have_text("Your Cart")

    print("Cancel checkout test passed")

