from playwright.sync_api import expect

def test_valid_login(login_page, page):
    login_page.goto()
    login_page.login("standard_user", "secret_sauce")

    expect(page).to_have_title("Swag Labs")