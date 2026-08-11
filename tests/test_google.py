import re # For Regular expression (Regex)
from playwright.sync_api import expect

def test_google_search(page):
    page.goto("http://127.0.0.1:8000/")

    expect(page).to_have_title(re.compile("PGH - STEP", re.IGNORECASE))