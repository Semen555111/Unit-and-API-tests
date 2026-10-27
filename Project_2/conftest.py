import pytest
from uuid import uuid4
from Project_2.pages.register_page import RegisterPage
from playwright.sync_api import Page, expect


@pytest.fixture
def user_data():
    return {
        "name": "QAStudent",
        "email": f"qa_{uuid4().hex[:12]}@example.com",
        "password": "TestPassword123!"
    }
@pytest.fixture
def login_user(page, user_data):
    register_page = RegisterPage(page)
    register_page.open()
    res = register_page.register(
        name=user_data["name"],
        email=user_data["email"],
        password=user_data["password"]
    )
    expect(
        register_page.register_success_message
    ).to_be_visible()

    return user_data

