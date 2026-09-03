from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class HomePage:

    def __init__(self, driver):
        self.driver = driver

    # ==========================================================
    # LOCATORS
    # ==========================================================

    LOGIN_BUTTON = (
        By.XPATH,
        "//button[@id='login-btn' and normalize-space()='Login']"
    )

    SIGNUP_BUTTON = (
        By.XPATH,
        "(//button[text()='Sign up'])[1]"
    )

    COURSES_MENU = (
        By.XPATH,
        "//header//*[text()='Courses'] | "
        "//nav//*[text()='Courses'] | "
        "(//*[text()='Courses'])[2]"
    )

    LIVE_CLASSES_MENU = (
        By.XPATH,
        "//*[contains(text(),'LIVE Classes') or "
        "contains(text(),'Zen Class')]"
    )

    PRACTICE_MENU = (
        By.XPATH,
        "//*[contains(text(),'Practice') or "
        "contains(@class, 'practice')]"
    )

    # Dobby Assistant
    DOBBY_ASSISTANT_BUTTON = (
        By.XPATH,
        "//span[contains(@class,'siqico-chat') "
        "and contains(@class,'zsiq-chat-icn')]"
    )

    # Profile Avatar
    PROFILE_AVATAR_MENU = (
        By.XPATH,
        "//*[contains(@class, 'avatar') "
        "or contains(@class, 'profile') "
        "or @aria-label='account of current user'] "
        "| //button[contains(@onclick, 'profile') "
        "or contains(@class, 'dropdown')]"
    )

    # Logout
    LOGOUT_ACTION_BUTTON = (By.ID, "signout")
    # ==========================================================
    # HOME PAGE ACTIONS
    # ==========================================================

    def open_home_page(self):
        self.driver.get("https://www.guvi.in/")

    def get_page_title(self):
        return self.driver.title

    def get_current_url(self):
        return self.driver.current_url

    # ==========================================================
    # LOGIN BUTTON
    # ==========================================================

    def is_login_button_displayed(self):
        """Checks whether Login button is visible."""

        try:
            element = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(
                    self.LOGIN_BUTTON
                )
            )

            return element.is_displayed()

        except TimeoutException:
            return False

    def click_login_button(self):
        """Clicks the visible Login button."""

        login_btn = WebDriverWait(
            self.driver,
            15
        ).until(
            EC.element_to_be_clickable(
                self.LOGIN_BUTTON
            )
        )

        print(
            "\n[Validation Log] "
            "Login button found and clickable."
        )

        login_btn.click()

    # ==========================================================
    # SIGN UP
    # ==========================================================

    def is_signup_button_displayed_and_clickable(self):
        """Checks whether Sign-up button is visible and clickable."""

        try:
            element = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(
                    self.SIGNUP_BUTTON
                )
            )

            return element.is_displayed()

        except TimeoutException:
            return False

    def click_signup(self):
        """Clicks Sign-up button."""

        if self.is_signup_button_displayed_and_clickable():

            self.driver.find_element(
                *self.SIGNUP_BUTTON
            ).click()

        else:
            raise AssertionError(
                "Sign-up button is either not displayed "
                "or not clickable."
            )

    # ==========================================================
    # SIGN UP PAGE
    # ==========================================================

    def is_signup_page_loaded_successfully(self):
        """Checks whether registration form is displayed."""

        try:
            registration_form = WebDriverWait(
                self.driver,
                10
            ).until(
                EC.visibility_of_element_located(
                    (By.TAG_NAME, "form")
                )
            )

            return registration_form.is_displayed()

        except TimeoutException:
            return False

    # ==========================================================
    # DASHBOARD
    # ==========================================================

    def is_dashboard_profile_loaded(self):
        """Checks whether dashboard/profile area is displayed."""

        try:
            profile_dashboard_element = WebDriverWait(
                self.driver,
                15
            ).until(
                EC.visibility_of_element_located(
                    (
                        By.XPATH,
                        "//*[contains(@class, 'profile') "
                        "or contains(text(), 'Dashboard')]"
                    )
                )
            )

            return profile_dashboard_element.is_displayed()

        except TimeoutException:
            return False

    # ==========================================================
    # HEADER VALIDATIONS
    # ==========================================================

    def is_courses_menu_visible(self):
        """Checks whether Courses menu is visible."""

        try:
            element = WebDriverWait(
                self.driver,
                10
            ).until(
                EC.visibility_of_element_located(
                    self.COURSES_MENU
                )
            )

            return element.is_displayed()

        except TimeoutException:
            return False

    def is_live_classes_menu_visible(self):
        """Checks whether LIVE Classes menu is visible."""

        try:
            element = WebDriverWait(
                self.driver,
                10
            ).until(
                EC.visibility_of_element_located(
                    self.LIVE_CLASSES_MENU
                )
            )

            return element.is_displayed()

        except TimeoutException:
            return False

    def is_practice_menu_visible(self):
        """Checks whether Practice menu is visible."""

        try:
            element = WebDriverWait(
                self.driver,
                10
            ).until(
                EC.visibility_of_element_located(
                    self.PRACTICE_MENU
                )
            )

            return element.is_displayed()

        except TimeoutException:
            return False

    # ==========================================================
    # DOBBY ASSISTANT
    # ==========================================================

    def is_dobby_assistant_displayed(self):
        """Checks whether Dobby Assistant is visible."""

        try:

            element = WebDriverWait(
                self.driver,
                15
            ).until(
                EC.visibility_of_element_located(
                    self.DOBBY_ASSISTANT_BUTTON
                )
            )

            print(
                f"\n[Validation Log] "
                f"Dobby Assistant Element Found: "
                f"{element.tag_name}"
            )

            return element.is_displayed()

        except TimeoutException:

            print(
                "\n[Validation Log] "
                "Dobby Assistant button was not found "
                "or was not visible."
            )

            return False

    # ==========================================================
    # PROFILE AVATAR
    # ==========================================================

    def click_profile_avatar(self):
        """Opens the profile dropdown menu."""

        avatar_btn = WebDriverWait(
            self.driver,
            15
        ).until(
            EC.presence_of_element_located(
                self.PROFILE_AVATAR_MENU
            )
        )

        print(
            "\n[Validation Log] "
            "Profile avatar found."
        )

        self.driver.execute_script(
            "arguments[0].click();",
            avatar_btn
        )

    # ==========================================================
    # LOGOUT
    # ==========================================================

    def click_logout_option(self):
        """Clicks the Sign Out option from the profile menu."""

        logout_btn = WebDriverWait(
            self.driver,
            10
        ).until(
            EC.presence_of_element_located(
                self.LOGOUT_ACTION_BUTTON
            )
        )

        print(
            f"\n[Validation Log] "
            f"Logout option found: {logout_btn.get_attribute('id')}"
        )

        self.driver.execute_script(
            "arguments[0].click();",
            logout_btn
        )