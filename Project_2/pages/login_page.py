from playwright.sync_api import Page


class LoginPage:

    URL = "https://practice.expandtesting.com/notes/app/login"

    def __init__(self, page: Page):
        self.page = page

        self.email_input = page.get_by_test_id("login-email")
        self.password_input = page.get_by_test_id("login-password")
        self.login_button = page.get_by_test_id("login-submit")


    def open(self):
        self.page.goto(self.URL)

    def login(self, email: str, password: str):
        self.email_input.fill(email)
        self.password_input.fill(password)
        self.login_button.click()