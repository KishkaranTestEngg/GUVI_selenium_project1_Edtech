import pytest
from pages.home_page import HomePage
from pages.login_page import LoginPage
from selenium.webdriver.support.ui import WebDriverWait


def test_tc006_login_button(driver):
    home_page = HomePage(driver)
    login_page = LoginPage(driver)

    # Step 1: Open the GUVI official landing page
    home_page.open_home_page()

    # Step 2: Navigate to the login screen
    home_page.click_login_button()

    # CRITICAL SYNC: Wait up to 15 seconds for the browser URL to switch to the sign-in page context
    WebDriverWait(driver, 15).until(
        lambda d: "sign-in" in d.current_url
    )

    # Step 3: Verify the login form fields are fully visible on screen before entering details
    assert login_page.is_email_field_visible(), "Email input field failed to render on the sign-in page."
    assert login_page.is_password_field_visible(), "Password input field failed to render on the sign-in page."
    assert login_page.is_login_button_visible(), "Submit login button failed to render on the sign-in page."

    # Step 4: Enter authentication credentials now that the page is loaded
    login_page.enter_email("kishkaranptestengineer@gmail.com")
    login_page.enter_password("Kishoretester@123")

    # Step 5: Submit the login form credentials
    login_page.click_submit_login()

    # Step 6: Wait for a brief moment for the backend authentication check to register
    import time
    time.sleep(5)

    # Step 7: Confirm that the user successfully left the sign-in page (Passed Authentication)
    actual_url = home_page.get_current_url()
    assert "sign-in" not in actual_url, (
        f"Authentication failed. The session remained stuck on the sign-in screen: {actual_url}"
    )

    print(f"\nSuccessfully Logged In! Redirected Landing URL: {actual_url}")
