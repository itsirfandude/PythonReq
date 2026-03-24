from playwright.sync_api import sync_playwright

def test_google():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        page.goto("https://example.com")

        assert "Example" in page.title()

        browser.close()



def test_login_success():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        page.goto("https://www.saucedemo.com")

        # Enter credentials
        page.fill("#user-name", "standard_user")
        page.fill("#password", "secret_sauce")

        # Click login
        page.click("#login-button")

        # Assert URL change
        assert "inventory" in page.url

        # Assert page content
        assert page.locator(".title").inner_text() == "Products"

        browser.close()

def test_login_failure():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        page.goto("https://www.saucedemo.com")

        page.fill("#user-name", "standard_user")
        page.fill("#password", "wrong_password")

        page.click("#login-button")

        # Assert still on login page
        assert "inventory" not in page.url

        # Assert error message
        error_text = page.locator(".error-message-container").inner_text()
        assert "do not match" in error_text.lower()

        browser.close()