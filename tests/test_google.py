import re # For Regular expression (Regex)
from playwright.sync_api import expect

def test_google_search(page):
    page.goto("https://www.google.com/")

    expect(page).to_have_title(re.compile("Google", re.IGNORECASE))