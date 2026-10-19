from uuid import uuid4
import pytest




@pytest.mark.usernegative
def test_api_register_negative(api_request_context, api_new_user):

    response = api_request_context.post(
        "/notes/api/users/register",
        form={
            "name": api_new_user["name"],
            "email": api_new_user["email"],
            "password": api_new_user["password"]
        }
    )
    assert response.status == 409
    data = response.json()
    assert data["success"] is False
    assert "already exists" in data["message"]
@pytest.mark.deleteuser
def test_api_delete_user(api_request_context, api_new_user):
    request = api_request_context
    email = api_new_user["email"]
    password = api_new_user["password"]
    login_response = request.post(
        "/notes/api/users/login",
        form={
            "email": email,
            "password": password
        }
    )

    assert login_response.status == 200
    login_data = login_response.json()
    token = login_data["data"]["token"]
    assert token
    delete_response = request.delete(
        "/notes/api/users/delete-account",
        headers={
            "x-auth-token": token
        }
    )
    assert delete_response.status == 200, delete_response.text()
    delete_data = delete_response.json()
    assert delete_data["success"] is True
    api_new_user["deleted"] = True