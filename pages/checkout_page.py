class CheckoutPage:

    # Checkout Information page ke locators
    first_name = "#first-name"
    last_name = "#last-name"
    postal_code = "#postal-code"
    continue_button = "#continue"
    error_message = "[data-test='error']"
    cancel_button = "#cancel"

    # Customer ki information fill karna
    def enter_checkout_information(self, page, first, last, postal):

        # First name enter karna
        page.locator(self.first_name).fill(first)

        # Last name enter karna
        page.locator(self.last_name).fill(last)

        # Portal code enter karo
        page.locator(self.postal_code).fill(postal)

    # Continue button per click karo
    def click_continue_button(self, page):
        page.locator(self.continue_button).click()


    # Error message return karna
    def get_error_message(self, page):
        return page.locator(self.error_message).inner_text()

    # Cancel button per click karna or verify karna ki cart page per wapas aana
    def click_cancel_button(self, page):
        page.locator(self.cancel_button).click()