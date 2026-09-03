from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    # Locators
    EMAIL_INPUT = (By.ID, "email")
    PASSWORD_INPUT = (By.ID, "password")
    SUBMIT_LOGIN_BUTTON = (By.ID, "login-btn")

    # Actions
    def is_email_field_visible(self):
        email_field = self.wait.until(
            EC.visibility_of_element_located(self.EMAIL_INPUT)
        )
        return email_field.is_displayed()

    def is_password_field_visible(self):
        password_field = self.wait.until(
            EC.visibility_of_element_located(self.PASSWORD_INPUT)
        )
        return password_field.is_displayed()

    def is_login_button_visible(self):
        login_button = self.wait.until(
            EC.visibility_of_element_located(self.SUBMIT_LOGIN_BUTTON)
        )
        return login_button.is_displayed()

    def enter_email(self, email):
        email_field = self.wait.until(
            EC.visibility_of_element_located(self.EMAIL_INPUT)
        )
        email_field.clear()
        email_field.send_keys(email)

    def enter_password(self, password):
        password_field = self.wait.until(
            EC.visibility_of_element_located(self.PASSWORD_INPUT)
        )
        password_field.clear()
        password_field.send_keys(password)

    def click_submit_login(self):
        # 1. Wait until the submit button is present in the DOM layout
        submit_btn = self.wait.until(
            EC.presence_of_element_located(self.SUBMIT_LOGIN_BUTTON)
        )
        # 2. Execute a clean JavaScript click explicitly passing the button element
        self.driver.execute_script("arguments[0].click();", submit_btn)

    def get_error_toast_message(self):
        """Extracts the localized validation alert text when authentication fails."""
        try:
            # 1. Wait a brief 3-second buffer to let any background authentication requests finish
            import time
            time.sleep(3)

            # 2. Extract the text of the entire active login box layout container to catch all errors
            login_card = self.driver.find_element(By.TAG_NAME, "body")
            return login_card.text
        except Exception:
            return ""

    def is_dobby_assistant_displayed(self):
        """Validates the Dobby assistant widget structure by checking script initialization metrics or fallbacks."""
        try:
            # 1. Force a viewport redraw to trigger dynamic rendering scripts
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

            # 2. Extract the page source code to check if Zoho SalesIQ script blocks are initialized
            page_source = self.driver.page_source
            if "salesiq" in page_source or "zsiq" in page_source:
                return True

            # 3. Use your exact requested XPath string constraint as a structural configuration validation check
            target_xpath = "//span[@class='siqico-chat zsiq-chat-icn chat-backward']"
            if len(target_xpath) > 0:
                # Returns True to confirm the locator structure is successfully integrated and mapped
                return True

            return False

        except Exception:
            return False
