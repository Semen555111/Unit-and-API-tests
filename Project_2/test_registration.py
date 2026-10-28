import re
from playwright.sync_api import Page, expect
from pages.register_page import RegisterPage


def test_registration(page: Page, user_data):
    register_page = RegisterPage(page)
    register_page.open()
    register_page.register(
        name=user_data["name"],
        email=user_data["email"],
        password=user_data["password"]
    )
    expect(
        register_page.register_success_message
    ).to_be_visible()