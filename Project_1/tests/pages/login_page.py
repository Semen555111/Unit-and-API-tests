from playwright.sync_api import Locator, Page


class LoginPage:
    """Page Object страницы входа Notes App."""

    URL = "https://practice.expandtesting.com/notes/app/login"

    def __init__(self, page: Page):
        self.page = page
        self.email_input: Locator = page.locator("#email")
        self.password_input: Locator = page.locator("#password")
        self.login_button: Locator = page.get_by_role(
            "button", name="Login", exact=True
        )

    def open(self) -> None:
        self.page.goto(self.URL, wait_until="domcontentloaded")

    def login(self, email: str, password: str) -> None:
        self.email_input.fill(email)
        self.password_input.fill(password)
        self.login_button.click()
