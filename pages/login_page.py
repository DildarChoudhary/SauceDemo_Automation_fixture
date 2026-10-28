
class LoginPage:

    # Locator
    username = "#user-name"
    password = "#password"
    login_button = "#login-button"

    # Login credentials
    valid_username = "standard_user"
    valid_password = "secret_sauce"
    invalid_username = "wrong_user"
    invalid_password = "wrong_password"

    def login(self, page, username, password):

    # SauceDemo website open karna
       page.goto("https://www.saucedemo.com/")

    # Username enter karo
       page.locator(self.username).fill(username)

    # Password enter karo
       page.locator(self.password).fill(password)

    # Login button per click karo
       page.locator(self.login_button).click()


