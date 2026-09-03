import pytest

from pages.home_page import HomePage
from pages.login_page import LoginPage

from selenium.webdriver.support.ui import WebDriverWait


def test_tc010_logout(driver):

    home_page = HomePage(driver)
    login_page = LoginPage(driver)

    # ==========================================================
    # STEP 1: Open GUVI Home Page
    # ==========================================================

    home_page.open_home_page()

    # ==========================================================
    # STEP 2: Click Login
    # ==========================================================

    home_page.click_login_button()

    # ==========================================================
    # STEP 3: Wait for Sign-in Page
    # ==========================================================

    WebDriverWait(driver, 15).until(
        lambda d: "sign-in" in d.current_url.lower()
    )

    print(
        f"\n[Execution Track] "
        f"Login Page URL: {driver.current_url}"
    )

    # ==========================================================
    # STEP 4: Enter Login Credentials
    # ==========================================================

    login_page.enter_email(
        "kishkaranptestengineer@gmail.com"
    )

    login_page.enter_password(
        "Kishoretester@123"
    )

    login_page.click_submit_login()

    # ==========================================================
    # STEP 5: Wait for Successful Login
    # ==========================================================

    WebDriverWait(driver, 20).until(
        lambda d: "sign-in" not in d.current_url.lower()
    )

    print(
        f"\n[Execution Track] "
        f"Post-Login URL: {driver.current_url}"
    )

    # ==========================================================
    # STEP 6: Open Profile Avatar
    # ==========================================================

    home_page.click_profile_avatar()

    # ==========================================================
    # STEP 7: Click Logout
    # ==========================================================

    home_page.click_logout_option()

    # ==========================================================
    # STEP 8: Wait for Logout Redirect
    # ==========================================================

    WebDriverWait(driver, 15).until(
        lambda d: (
            "sign-in" in d.current_url.lower()
            or "login" in d.current_url.lower()
            or d.current_url.lower().rstrip("/")
            == "https://www.guvi.in"
        )
    )

    # ==========================================================
    # STEP 9: Get Final URL
    # ==========================================================

    final_url = home_page.get_current_url()

    print(
        f"\n[Execution Track] "
        f"Post-Logout Active Landing URL: {final_url}"
    )

    # ==========================================================
    # STEP 10: Validate Logout
    # ==========================================================

    assert (
        "sign-in" in final_url.lower()
        or "login" in final_url.lower()
        or final_url.lower().rstrip("/")
        == "https://www.guvi.in"
    ), (
        "Logout validation failed! "
        f"Current URL after logout: {final_url}"
    )

    print(
        "\n[Validation Result] "
        "Logout functionality verified successfully."
    )