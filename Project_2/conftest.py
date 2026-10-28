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


@pytest.fixture
def api_request_context(playwright):

    request = playwright.request.new_context(
        base_url="https://practice.expandtesting.com",
        extra_http_headers={
            "Accept": "application/json"
        }
    )

    yield request
    request.dispose()


@pytest.fixture
def api_new_user(api_request_context, user_data):

    request = api_request_context
    response = request.post(
        "/notes/api/users/register",
        form={
            "name": user_data["name"],
            "email": user_data["email"],
            "password": user_data["password"]
        }
    )
    assert response.status == 201, response.text()
    user = {
        "name": user_data["name"],
        "email": user_data["email"],
        "password": user_data["password"],
        "registration_response": response,
        "deleted": False
    }
    yield user
    if not user["deleted"]:

        login_response = request.post(
            "/notes/api/users/login",
            form={
                "email": user_data["email"],
                "password": user_data["password"]
            }
        )
        assert login_response.status == 200, login_response.text()
        token = login_response.json()["data"]["token"]
        delete_response = request.delete(
            "/notes/api/users/delete-account",
            headers={
                "x-auth-token": token
            }
        )
        assert delete_response.status == 200, delete_response.text()