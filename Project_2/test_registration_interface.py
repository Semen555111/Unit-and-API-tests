import re
from playwright.sync_api import Page, expect
from Project_2.pages.register_page import RegisterPage


def test_example(page: Page) -> None:
    register_page = RegisterPage(page)
    register_page.open()
    expect(page.get_by_test_id("register-email")).to_be_visible()
    expect(page.get_by_test_id("register-name")).to_be_visible()
    expect(page.get_by_test_id("register-password")).to_be_visible()
    expect(page.get_by_test_id("register-confirm-password")).to_be_visible()
    expect(page.get_by_test_id("register-submit")).to_be_visible()

