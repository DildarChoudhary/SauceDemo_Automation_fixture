from pages.login_page import LoginPage
from pages.products_page import ProductsPage

def test_products_page(products_page):

    page = products_page

    # ProductPage ka object banana
    products_page = ProductsPage()

    # Products page ka title check karna
    assert products_page.get_product_title(page)== "Products"

    # Sabhi products ke naam lena
    product_names = products_page.get_product_names(page)

    # Sabi product k prices lena
    product_prices = products_page.get_product_prices(page)

    # Products aur prices terminal mein print karna
    print("product_names: ", product_names)
    print("product_prices: ", product_prices)

    # Check karna ki 6 products aur 6 prices hain
    assert len(product_names) == 6
    assert len(product_prices) == 6

# Empty cart ko open karna or verify karna
def test_empty_cart(products_page):
    page = products_page

    # ProductsPage ka object banana
    products = ProductsPage()

    # Bina product add kiye cart open karna
    products.open_cart(page)

    # Check karna ki cart mein koi product nahi hai
    assert page.locator(".cart_item").count() == 0


# Sauce Labs Backpack ko cart mein add karne ka test
def test_add_product_to_cart(products_page):

    page = products_page

    # ProductsPage ka object banana
    products_page = ProductsPage()

    # Backpack ko cart mein add karna
    products_page.add_to_cart(page, "Sauce Labs Backpack")

    #Sauce Labs Bike Light add karna
    products_page.add_to_cart(page, "Sauce Labs Bike Light")

    # Sauce Labs Bolt T-Shirt
    products_page.add_to_cart(page, "Sauce Labs Bolt T-Shirt")

    # Cart icon par product count 1 hai ya nahi check karna
    cart_count = page.locator(".shopping_cart_badge").inner_text()
    assert cart_count == "3"

    # Cart icon par click karke Cart page open karna
    products_page.open_cart(page)

# Selected product ko remove karne ka test
def test_remove_product_from_products_page(products_page):

    page = products_page

    # ProductPage ka object banana
    products_page = ProductsPage()

    # Backpack ko cart mein add karna
    products_page.add_to_cart(page, "Sauce Labs Backpack")

    # Verify karna ki cart badge par 1 hai
    assert page.locator(".shopping_cart_badge").inner_text() == "1"

    # Backpack ko Products page se remove karna
    products_page.remove_from_cart(page, "Sauce Labs Backpack")

    # Verify karna ki cart badge ab nahi hai
    assert page.locator(".shopping_cart_badge").count() == 0


