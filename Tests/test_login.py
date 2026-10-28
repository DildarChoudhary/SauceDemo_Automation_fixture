
# LoginPage class ko import karna
from pages.login_page import LoginPage

# Valid login test
def test_valid_login(page):

    # LoginPage class ka object banana
    login_page = LoginPage()

    # Valid username aur password se login karna
    login_page.login(
         page,
         login_page.valid_username,
         login_page.valid_password
    )

    # Check karna ki Products page open hua hai
    assert page.locator(".title").inner_text() == "Products"

# Invalid login test
def test_invalid_login(page):
    login_page = LoginPage()

    login_page.login(
        page,
        login_page.invalid_username,
        login_page.invalid_password
    )

    # Error message ka text lena
    error_message = page.locator("[data-test='error']").inner_text()

    print("\n error msg: ", error_message)

    # Error mag verify karna
    assert "Username and password do not match" in error_message

    # Verify karna ki expected error message aaya hai
    assert "Username and password do not match any user in this service" in error_message

# Blank username aur password test
def test_blank_login(page):
    # LoginPage class ka object banana
    login_page = LoginPage()

    # Username aur password dono khaali rakhkar login karna
    login_page.login(page, "", "")

    # Website ka error message lena
    error_message = page.locator("[data-test='error']").inner_text()

    # Actual error message terminal mein print karna
    print(error_message)

    # Verify karna ki username required error aaya hai
    assert "Username is required" in error_message


# Blank password test
def test_blank_password(page):

    # LoginPage class ka object banana
    login_page = LoginPage()

    # Valid username ke saath blank password se login karna
    login_page.login(
        page,
        login_page.valid_username,
        ""
    )

    # Website ka error message lena
    error_message = page.locator("[data-test='error']").inner_text()

    # Actual error message terminal mein print karna
    print(error_message)

    # Verify karna ki password required error aaya hai
    assert "Password is required" in error_message