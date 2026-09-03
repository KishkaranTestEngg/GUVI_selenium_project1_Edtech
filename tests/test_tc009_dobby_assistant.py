import pytest
from pages.home_page import HomePage


def test_tc009_dobby_assistant(driver):
    home_page = HomePage(driver)

    # Step 1: Open the official HCL GUVI landing page environment
    home_page.open_home_page()

    # Step 2: Query the page object layer for the floating helper bubble status
    assistant_visible = home_page.is_dobby_assistant_displayed()

    # Step 3: Print a clear log output for transparency
    print(f"\n[Validation Log] Dobby GUVI Assistant Display Status: {assistant_visible}")

    # Step 4: Core Assertion to confirm the automated assistant is visible to users
    assert assistant_visible, (
        "Test Failed: The Dobby GUVI Assistant floating widget button was missing or failed to render on screen!"
    )
