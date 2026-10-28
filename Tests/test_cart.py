from playwright.sync_api import expect
from pages.login_page import LoginPage
from pages.products_page import ProductsPage
from pages.cart_page import CartPage

# Cart page test karna
def test_cart_page(cart_page):

    page = cart_page

    # CartPage ka object banana
    cart_page = CartPage()

    # Cart page ka title check karna
    #assert cart_page.get_cart_title(page) == "Your Cart"
    expect(page.locator(".title")).to_have_text("Your Cart")

    # Cart mein products ke naam lena
    cart_products_names = cart_page.get_cart_product_names(page)

    # Cart mein products ki prices lena
    cart_products_prices = cart_page.get_cart_product_prices(page)

    # Check karna ki Backpack cart mein hai
    assert "Sauce Labs Backpack" in cart_products_names

    # Check karna ki prices cart mein hai
    assert "$29.99" in cart_products_prices

    # Cart products terminal mein print karna
    print("Cart Products:", cart_products_names)

    # Cart products prices terminal mein print karna
    print("cart products prices:", cart_products_prices)

    # Checkout button per click karna
    cart_page.click_checkout_button(page)

# Continue Shopping karke doosra product add karna
def test_continue_shopping_add_another_product(cart_page):

    page = cart_page

    # ProductsPage/CartPage ka object banana
    products_page = ProductsPage()
    cart_page = CartPage()

    # Continue button per click karna
    cart_page.click_continue_shopping_button(page)

    # Products page se second project add karna
    products_page.add_to_cart(page, "Sauce Labs Bike Light")

    # Cart page dubara open karna
    products_page.open_cart(page)

    # cart page se product k name lena
    cart_product_names=cart_page.get_cart_product_names(page)

    # Check karna ki Backpack aur Bike Light dono cart mein hain
    assert "Sauce Labs Backpack" in cart_product_names
    assert "Sauce Labs Bike Light" in cart_product_names

    # Debugging cart state in WebKit
    print("Current URL:", page.url)
    print("Cart item count:", page.locator(".cart_item").count())
    print("Cart product names:", cart_product_names)
    print("Cart page text:", page.locator("body").inner_text())

    page.wait_for_timeout(60000)

    # Check karna ki cart mein total 2 products hain
    assert page.locator(".cart_item").count() == 2

    # Terminal mein product names print karna
    print("Cart Products:", cart_product_names)


# Continue shopPing karke dusra product add to cart karna fir cart page se remove karna
def test_remove_products_from_cart(cart_page):

    page = cart_page

    # ProductPage and CartPage class ka object banao
    products_page = ProductsPage()
    cart_page = CartPage()

    # Continue button per click karna
    cart_page.click_continue_shopping_button(page)

    # product page se dusra product add karna
    products_page.add_to_cart(page, "Sauce Labs Bike Light")

    # cart page dubara open karna
    products_page.open_cart(page)

    # cart page se products name lena
    cart_product_names=cart_page.get_cart_product_names(page)

    # Check karna ki Backpack aur Bike Light dono cart mein hain
    assert "Sauce Labs Backpack" in cart_product_names
    assert "Sauce Labs Bike Light" in cart_product_names

    # Check karna ki cart mein total 2 products hain
    expect(page.locator(".cart_item")).to_have_count(2)

    # Backpack remove karna
    cart_page.remove_product(page, "Sauce Labs Backpack")

    # Verify karna ki ab sirf 1 product hai
    assert page.locator(".cart_item").count() == 1

    # Bike light remove karna
    cart_page.remove_product(page, "Sauce Labs Bike Light")

    # Verify karna ki cart empty hai
    assert page.locator(".cart_item").count() == 0

    # print karo ki product 0 hain
    print("Cart Products: cart product is zero")








