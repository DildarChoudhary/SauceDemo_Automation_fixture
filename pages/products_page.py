class ProductsPage:


    # Products page ke locators
    page_title = ".title"
    product_names = ".inventory_item_name"
    product_prices = ".inventory_item_price"
    cart_icon = ".shopping_cart_link"

    # Products page ka title return karna
    def get_product_title(self, page):
        return page.locator(self.page_title).inner_text()

    # Page par available products ke naam return karna
    def get_product_names(self, page):
        return page.locator(self.product_names).all_inner_texts()

    # Page par available products ki prices return karna
    def get_product_prices(self, page):
        return page.locator(self.product_prices).all_inner_texts()

    # Specific product ko cart mein add karna
    def add_to_cart(self, page, product_name):

        # Product ke naam ke basis par uska Add to cart button locate karna
        product = page.locator(".inventory_item").filter(
            has=page.locator(".inventory_item_name", has_text=product_name)
        )

        # Usi product ka Add to cart button click karna
        product.get_by_role("button", name="Add to cart").click()

    # Cart icon par click karke Cart page open karna
    def open_cart(self, page):
        page.locator(self.cart_icon).click()

    # Selected product ko cart se remove karna
    def remove_from_cart(self, page, product_name):

        # Product ke naam se uska container locate karna
        product = page.locator(".inventory_item").filter(
            has=page.locator(
                ".inventory_item_name",
                has_text=product_name
            )
        )

        # Selected product ka Remove button click karna
        product.get_by_role("button", name="Remove").click()