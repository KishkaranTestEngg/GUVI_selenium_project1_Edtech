from pages.home_page import HomePage


def test_guvi_login_button(driver):
    home_page = HomePage(driver)

    home_page.open_home_page()
    home_page.click_login_button()

    print("Current URL after Login click:", driver.current_url)