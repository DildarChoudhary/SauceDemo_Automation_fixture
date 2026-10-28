
class CartPage:

    # Cart page ke locators
    cart_title = ".title"
    cart_product_names = ".inventory_item_name"
    cart_product_prices = ".inventory_item_price"
    checkout_button = "#checkout"
    continue_shopping_button = ".btn.btn_secondary.back.btn_medium"

    # Cart page ka title return karna
    def get_cart_title(self, page):
        return page.locator(self.cart_title).inner_text()

    # Cart mein available products ke naam return karna
    def get_cart_product_names(self, page):
        return page.locator(self.cart_product_names).all_inner_texts()

    # Cart me available products ki price return karana
    def get_cart_product_prices(self, page):
        return page.locator(self.cart_product_prices).all_inner_texts()

    # Checkout button par click karna
    def click_checkout_button(self, page):
        page.locator(self.checkout_button).click()

    # Continue Shopping button per click karna
    def click_continue_shopping_button(self, page):
        page.locator(self.continue_shopping_button).click()

    # Cart page se selected product remove karna
    def remove_product(self, page, product_name):
        # Product ke naam se cart item locate karna
        product = page.locator(".cart_item").filter(
            has=page.locator(
                ".inventory_item_name",
                has_text=product_name
            )
        )

        # Selected product ka Remove button click karna
        product.get_by_role("button", name="Remove").click()