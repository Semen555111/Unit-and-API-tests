import re
import pytest
from playwright.sync_api import Page, expect

def test_login_api(api_request_context, api_new_user):
    user =api_new_user
    response = api_request_context.post(