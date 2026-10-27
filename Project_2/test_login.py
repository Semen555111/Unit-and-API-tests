import re
from playwright.sync_api import Page, expect
from Project_2.pages.register_page import RegisterPage
from Project_2.pages.login_page import LoginPage


def test_login(page: Page, user_data, login_user):
    login_page = LoginPage(page)
    login_page.open()
    login_page.login(
        email=login_user["email"],
        password=login_user["password"]
    )
    expect(page.get_by_test_id("home")).to_be_visible()



    