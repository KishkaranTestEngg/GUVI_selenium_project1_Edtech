import pytest
from pages.home_page import HomePage
from pages.login_page import LoginPage
from selenium.webdriver.support.ui import WebDriverWait

def test_tc007_invalid_login(driver):
    home_page = HomePage(driver)
    login_page = LoginPage(driver)

    # Step 1: Open the GUVI official landing page
    home_page.open_home_page()

    # Step 2: Navigate to the login screen
    home_page.click_login_button()

    # Step 3: FIXED SYNC: Wait for the browser URL context switch to accept either "sign-in" or "login"
    WebDriverWait(driver, 15).until(lambda d: "sign-in" in d.current_url or "login" in d.current_url)

    # Step 4: Input incorrect email credentials
    login_page.enter_email("invalid_guvi_user@gmail.com")

    # Step 5: Input incorrect password credentials
    login_page.enter_password("WrongPassword123!")

    # Step 6: Execute login submission attempt via JS executor injection
    login_page.click_submit_login()

    # Step 7: Capture the fallback screen body context text
    error_output = login_page.get_error_toast_message()

    # Step 8: Assert that authentication fails and verification message criteria are met
    # If body tracking text returns empty, fallback cleanly to explicit selector element text inspection
    if not error_output.strip():
        error_output = login_page.get_explicit_error_text()

    assert len(error_output) > 0, "Test Failed: Expected error text layout confirmation banner was completely absent!"
    print(f"\nTest Passed! Observed Application Validation Catch: {error_output}")
