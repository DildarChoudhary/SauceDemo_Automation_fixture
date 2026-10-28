class CheckoutCompletePage:

   # Checkout Complete page ke locators
   page_title = ".title"
   complete_header = ".complete-header"
   complete_text = ".complete-text"
   back_home_button = "#back-to-products"
   generate_pdf = "#generate-pdf-order"


   # Page title return karna
   def get_page_title(self, page):
       return page.locator(self.page_title).inner_text()


   # Order confirmation heading return karna
   def get_complete_header(self, page):
       return page.locator(self.complete_header).inner_text()


   # Confirmation message return karna
   def get_complete_text(self, page):
       return page.locator(self.complete_text).inner_text()

   # PDF generate karna
   def click_on_pdf_button(self, page):
       page.locator(self.generate_pdf).click()

   # Products page par wapas jana
   def click_back_home(self, page):
       page.locator(self.back_home_button).click()