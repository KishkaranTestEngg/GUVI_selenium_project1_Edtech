# Open tests/conftest.py
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture
def driver():
    options = Options()

    # 1. Mask automation markers to bypass bot filters
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option("useAutomationExtension", False)
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_argument("--start-maximized")

    # 2. CRITICAL FIX: Turn off Chrome's native password manager and popups globally
    prefs = {
        "credentials_enable_service": False,  # Disables the "Save password?" prompt entirely
        "profile.password_manager_enabled": False,  # Prevents password manager overlays
    }
    options.add_experimental_option("prefs", prefs)

    # Initialize the customized session framework
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)

    yield driver
    driver.quit()
