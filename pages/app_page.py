from selenium.webdriver.common.by import By
from base.selenium_driver import SeleniumDriver


class AppPage(SeleniumDriver):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # locators
    _login_page_btn = (By.CSS_SELECTOR, ".sign-in-form > button[type='submit']")

    def wait_for_url_change(self):
        self.wait_for_desired_url("https://app.fiscalnote.com/?error=notauthorized")

    def navigate_to_login_page(self):
        login_page_btn = self.wait_for_element(self._login_page_btn)
        self.click_element(None, login_page_btn)
