from pages.home_page import HomePage


def test_guvi_page_validation(driver):
    home_page = HomePage(driver)

    home_page.open_home_page()

    print("Current URL:", home_page.get_current_url())
    print("Page Title:", home_page.get_page_title())

    assert home_page.get_current_url() == "https://www.guvi.in/"
    assert "GUVI" in home_page.get_page_title()