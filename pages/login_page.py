from selenium.webdriver.common.by import By
from base.selenium_driver import SeleniumDriver
from selenium.webdriver.support import expected_conditions as EC
import time


class LoginPage(SeleniumDriver):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # locators
    _username_field = (By.CSS_SELECTOR, "input[name='email']")
    _password_field = (By.CSS_SELECTOR, "input[name='password']")
    _login_btn = (By.CSS_SELECTOR, ".auth0-lock-submit")
    _invalid_login_err_msg = (By.XPATH, "//span[contains(text(),'Wrong email or password.')]")
    _blank_username_err_msg = (By.XPATH, "//div[contains(@class, 'input-email')]/div/span[contains(text(), 'be blank')]")
    _blank_password_err_msg = (By.XPATH, "//div[contains(@class, 'input-password')]/div/span[contains(text(), 'be blank')]")

    def enter_username(self, username):
        username_field = self.wait_for_element_ec(self._username_field, EC.element_to_be_clickable)
        self.send_keys(username, None, username_field)

    def enter_password(self, password):
        password_field = self.wait_for_element_ec(self._password_field, EC.element_to_be_clickable)
        self.send_keys(password, None, password_field)

    def clear_input_fields(self):
        username_field = self.wait_for_element_ec(self._username_field, EC.element_to_be_clickable)
        password_field = self.wait_for_element_ec(self._password_field, EC.element_to_be_clickable)

        username_field.click()
        self.clear_field(None, username_field)

        password_field.click()
        self.clear_field(None, password_field)

    def click_login_btn(self):
        login_btn = self.wait_for_element(self._login_btn)
        self.click_element(None, login_btn)

    def login(self, username, password):
        username_field = self.wait_for_element(self._username_field)
        password_field = self.wait_for_element(self._password_field)
        self.send_keys(username, None, username_field)
        self.send_keys(password, None, password_field)
        self.click_login_btn()

    def verify_invalid_login(self):
        invalid_login_err_msg = self.wait_for_element(self._invalid_login_err_msg)
        return self.is_element_present(None, invalid_login_err_msg)

    def verify_blank_username_login(self):
        blank_username_err_msg = self.wait_for_element(self._blank_username_err_msg)
        return self.is_element_present(None, blank_username_err_msg)

    def verify_blank_password_login(self):
        blank_password_err_msg = self.wait_for_element(self._blank_password_err_msg)
        return self.is_element_present(None, blank_password_err_msg)

    def verify_blank_username_and_password_login(self):
        blank_username_err_msg = self.wait_for_element(self._blank_username_err_msg)
        blank_password_err_msg = self.wait_for_element(self._blank_password_err_msg)
        return self.is_element_present(None, blank_username_err_msg) and self.is_element_present(None, blank_password_err_msg)
