from playwright.sync_api import expect
from pages.checkout_complete_page import CheckoutCompletePage

def test_checkout_complete_page(checkout_complete_page):

    page = checkout_complete_page

    # CheckoutCompletePage ka object banao
    complete_page = CheckoutCompletePage()

    # page title verify karna
    #assert complete_page.get_page_title(page) == "Checkout: Complete!"
    expect(page.locator(".title")).to_have_text("Checkout: Complete!")

    # Confirmation heading verify karna
    assert complete_page.get_complete_header(page) == "Thank you for your order!"

    # Confirmation message verify karna
    assert complete_page.get_complete_text(page) == "Your order has been dispatched, and will arrive just as fast as the pony can get there!"

    # Confirmation message verify karna
    message = complete_page.get_complete_text(page)
    assert "Your order has been dispatched" in message

    print("Checkout complete page test passed")


# Test 2: Back Home button verify karna
def test_back_home(checkout_complete_page):

    page = checkout_complete_page

    # CheckoutCompletePage ka object banana
    complete_page = CheckoutCompletePage()

    # Back Home par click karna
    complete_page.click_back_home(page)

    # Products page verify karna
    #assert page.locator(".title").inner_text() == "Products"
    expect(page.locator(".title")).to_have_text("Products")

    print("Back Home test passed")

# Pdf generate karna
def test_pdf_generate(checkout_complete_page):

    page = checkout_complete_page

    # CheckoutCompletePage ka object banana
    complete_page = CheckoutCompletePage()

    # Pdf button per click karna
    complete_page.click_on_pdf_button(page)

    print("Pdf generation test passed")

