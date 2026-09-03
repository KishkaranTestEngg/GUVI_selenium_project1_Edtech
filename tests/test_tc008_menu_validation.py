import pytest
from pages.home_page import HomePage

def test_tc008_menu_validation(driver):
    home_page = HomePage(driver)

    # Step 1: Navigate to the official HCL GUVI homepage context layout
    home_page.open_home_page()

    # Step 2: Extract layout presence statuses across all three core nav items
    courses_visible = home_page.is_courses_menu_visible()
    live_classes_visible = home_page.is_live_classes_menu_visible()
    practice_visible = home_page.is_practice_menu_visible()

    # Step 3: Print operational log validation to trace component checks
    print(f"\n[Validation Log] 'Courses' Visibility Status: {courses_visible}")
    print(f"[Validation Log] 'LIVE Classes' Visibility Status: {live_classes_visible}")
    print(f"[Validation Log] 'Practice' Visibility Status: {practice_visible}")

    # Step 4: Core Assertion Checks to verify that all targets are fully visible and accessible
    assert courses_visible, "Test Failed: 'Courses' menu link element was hidden or missing from the homepage navbar layout!"
    assert live_classes_visible, "Test Failed: 'LIVE Classes' menu element was hidden or missing from the homepage navbar layout!"
    assert practice_visible, "Test Failed: 'Practice' header option element was hidden or missing from the homepage navbar layout!"

    print("\nTest Passed! All mandatory core navigation items ('Courses', 'LIVE Classes', 'Practice') are visible and accessible.")
