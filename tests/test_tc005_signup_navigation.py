from pages.home_page import HomePage
from selenium.webdriver.support.ui import WebDriverWait


def test_tc005_signup_navigation(driver):
    home_page = HomePage(driver)

    # Step 1: Open the GUVI official landing page
    home_page.open_home_page()

    # Step 2: Validate the initial button presence before execution
    assert home_page.is_signup_button_displayed_and_clickable(), (
        "Pre-condition failed: Sign-up button is missing or unclickable."
    )

    # Step 3: Trigger the navigation redirect event
    home_page.click_signup()

    # Step 4: Wait for the routing engine to transition to the registration endpoint context
    WebDriverWait(driver, 12).until(
        lambda d: "register" in d.current_url
    )

    # Step 5: Assert that the redirected URL string matches the specification target
    actual_url = home_page.get_current_url()
    assert "guvi.in/register" in actual_url, (
        f"Redirection URL mismatch. Expected target 'guvi.in/register' but landed on: {actual_url}"
    )

    # Step 6: Assert that the registration layout page context loaded successfully
    assert home_page.is_signup_page_loaded_successfully(), (
        "The registration landing page did not load its functional UI components properly."
    )
