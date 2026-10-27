from playwright.sync_api import Locator, Page


class RegisterPage:
    """Page Object страницы регистрации Notes App."""

    URL = "https://practice.expandtesting.com/notes/app/register"

    def __init__(self, page: Page):
        self.page = page
        self.email_input: Locator = page.locator("#email")
        self.name_input: Locator = page.locator("#name")
        self.password_input: Locator = page.locator("#password")
        self.confirm_password_input: Locator = page.locator("#confirmPassword")
        self.register_button: Locator = page.get_by_role(
            "button", name="Register", exact=True
        )
        self.success_message: Locator = page.get_by_text(
            "User account created successfully", exact=True
        )

    def open(self) -> None:
        self.page.goto(self.URL, wait_until="domcontentloaded")

    def register(self, name: str, email: str, password: str) -> None:
        self.email_input.fill(email)
        self.name_input.fill(name)
        self.password_input.fill(password)
        self.confirm_password_input.fill(password)
        self.register_button.click()
