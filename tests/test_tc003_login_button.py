from selenium.webdriver.support.wait import WebDriverWait
from pages.home_page import HomePage


def test_tc003_login_button(driver):
    home_page = HomePage(driver)

    home_page.open_home_page()

    assert home_page.is_login_button_displayed()

    home_page.click_login_button()

    WebDriverWait(driver, 15).until(
        lambda d: "sign-in" in d.current_url.lower()
    )

    print(
        "URL after clicking Login:",
        driver.current_url
    )

    assert "sign-in" in driver.current_url.lower()