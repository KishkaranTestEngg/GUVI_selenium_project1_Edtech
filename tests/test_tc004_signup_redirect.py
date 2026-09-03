import pytest
from pages.home_page import HomePage
from selenium.webdriver.support.ui import WebDriverWait


def test_tc004_signup_redirect(driver):
    home_page = HomePage(driver)

    # 1. Navigate to the homepage
    home_page.open_home_page()

    # 2. Verify button is displayed and clickable
    assert home_page.is_signup_button_displayed_and_clickable(), "Sign-up button check failed!"

    # 3. Click the button
    home_page.click_signup()

    # 4. Wait for the URL transition to the register page context
    WebDriverWait(driver, 10).until(
        lambda d: "register" in d.current_url
    )

    # 5. Assert the final landing page url matches
    assert "/register" in home_page.get_current_url(), f"Redirection failed. URL is: {home_page.get_current_url()}"
