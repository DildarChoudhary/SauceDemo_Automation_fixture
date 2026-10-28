class CheckoutOverviewPage:

    # Checkout Overview page ke locators
    page_title = ".title"
    product_names = ".inventory_item_name"
    product_prices = ".inventory_item_price"
    subtotal = ".summary_subtotal_label"
    tax = ".summary_tax_label"
    total = ".summary_total_label"
    finish_button = "#finish"
    cancel_button = "#cancel"

    # page ka title return karna
    def get_page_title(self, page):
        return page.locator(self.page_title).inner_text()

    # Products ka name return karna
    def get_product_names(self, page):
        return page.locator(self.product_names).all_inner_texts()

    # Product ki prices return karna
    def get_product_prices(self, page):
        return page.locator(self.product_prices).all_inner_texts()

    # Item subtotal return karna
    def get_subtotal(self, page):
        return page.locator(self.subtotal).inner_text()

    # Tax return karna
    def get_tax(self, page):
        return page.locator(self.tax).inner_text()

    # Final total return karna
    def get_total(self, page):
        return page.locator(self.total).inner_text()

    # Finish button par click karna
    def click_finish_button(self, page):
        page.locator(self.finish_button).click()

    # Cancel button per click karna
    def click_cancel_button(self, page):
        page.locator(self.cancel_button).click()


