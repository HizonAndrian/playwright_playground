import pytest
from pages.login_page import LogInPage

@pytest.fixture
def login_page(page):
    return LogInPage(page)