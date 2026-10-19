from uuid import uuid4
from dataclasses import dataclass

import pytest
from playwright.sync_api import Browser, Page


@dataclass
class NotesWorkflow:
    page: Page
    email: str
    password: str
    title: str
    original_text: str
    updated_text: str




@pytest.fixture(scope="module")
def notes_workflow(browser: Browser) -> NotesWorkflow:
    """Один пользователь и одна вкладка для трёх последовательных UI-тестов."""
    context = browser.new_context()
    page = context.new_page()
    unique_id = uuid4().hex[:10]
    workflow = NotesWorkflow(
        page=page,
        email=f"qa_notes_{unique_id}@example.com",
        password="TestPassword123!",
        title=f"POM note {unique_id}",
        original_text="Первоначальный текст тестовой заметки.",
        updated_text="Обновлённый текст тестовой заметки.",
    )
    yield workflow
    context.close()
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
def api_new_user(api_request_context):

    request = api_request_context

    name = "QAStudent"
    email = f"qa_{uuid4().hex[:12]}@example.com"
    password = "TestPassword123!"

    # Регистрируем нового пользователя
    response = request.post(
        "/notes/api/users/register",
        form={
            "name": name,
            "email": email,
            "password": password
        }
    )

    assert response.status == 201, response.text()

    user = {
        "name": name,
        "email": email,
        "password": password,
        "registration_response": response,
        "deleted": False
    }

    yield user

    # Очистка после завершения теста
    if not user["deleted"]:

        login_response = request.post(
            "/notes/api/users/login",
            form={
                "email": email,
                "password": password
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