import re # For Regular expression (Regex)
import pytest
from playwright.sync_api import Page, expect

def test_google_search(page: Page):
    page.goto("https://google.com")

    expect(page).to_have_title(re.compile("Google", re.IGNORECASE))