from selenium.webdriver.common.by import By
from base.selenium_driver import SeleniumDriver


class LoginPage(SeleniumDriver):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # locators
    _username_field = (By.CSS_SELECTOR, "input[name='email']")
    _password_field = (By.CSS_SELECTOR, "input[name='password']")
    _login_btn = (By.CSS_SELECTOR, ".auth0-lock-submit")

    _welcome_msg = (By.XPATH, "//h1[contains(., 'Welcome')]")
    _hovered_settings_btn = (By.CSS_SELECTOR, "div[class='ember-view sidebar-elem force-hover']")
    _account_menu = (By.CSS_SELECTOR, "#ember1321")
    _logout_btn = (By.CSS_SELECTOR, "a[class='logout']:nth-child(1)")

    def enter_username(self, username):
        username_field = self.wait_for_element(self._username_field)
        username_field.clear()
        self.send_keys(username, None, username_field)

    def enter_password(self, password):
        password_field = self.wait_for_element(self._password_field)
        password_field.clear()
        self.send_keys(password, None, password_field)

    def clear_fields(self):
        self.enter_username("")
        self.enter_password("")
