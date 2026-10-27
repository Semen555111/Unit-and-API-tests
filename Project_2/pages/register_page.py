from playwright.sync_api import Page


class RegisterPage:

    URL = "https://practice.expandtesting.com/notes/app/register"

    def __init__(self, page: Page):
        self.page = page

        self.email_input = page.get_by_test_id("register-email")
        self.name_input = page.get_by_test_id("register-name")
        self.password_input = page.get_by_test_id("register-password")
        self.confirm_password_input = page.get_by_test_id(
            "register-confirm-password"
        )
        self.register_button = page.get_by_test_id("register-submit")
        self.register_success_message = page.get_by_text(
        "User account created successfully",
        exact=True
)

    def open(self):
        self.page.goto(self.URL)

    def register(self, name: str, email: str, password: str):
        self.name_input.fill(name)
        self.email_input.fill(email)
        self.password_input.fill(password)
        self.confirm_password_input.fill(password)
        self.register_button.click()