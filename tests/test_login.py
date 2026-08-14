from playwright.sync_api import expect

def test_standard_login(login_page, page):
    login_page.goto()
    login_page.login("standard_user", "secret_sauce")

    expect(page).to_have_title("Swag Labs")

def test_locked_login(login_page, page):
    login_page.goto()
    login_page.login("locked_out_user", "secret_sauce")

    expect(page).to_have_title("Swag Labs")

def test_problem_login(login_page, page):
    login_page.goto()
    login_page.login("problem_user", "secret_sauce")

    expect(page).to_have_title("Swag Labs")

def test_performance_login(login_page, page):
    login_page.goto()
    login_page.login("performance_glitch_user", "secret_sauce")

    expect(page).to_have_title("Swag Labs")

def test_error_login(login_page, page):
    login_page.goto()
    login_page.login("error_user", "secret_sauce")

    expect(page).to_have_title("Swag Labs")

def test_visual_login(login_page, page):
    login_page.goto()
    login_page.login("visual_user", "secret_sauce")

    expect(page).to_have_title("Swag Labs")