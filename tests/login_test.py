from pages.app_page import AppPage
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from utilities.status import Status
import unittest
import pytest
from utilities.credentials import get_username, get_password, get_invalid_username, get_invalid_password


@pytest.mark.usefixtures('class_setup')
class LoginTest(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def object_setup(self):
        self.app_page = AppPage(self.driver)
        self.login_page = LoginPage(self.driver)
        self.dashboard_page = DashboardPage(self.driver)
        self.status = Status(self.driver)

    @pytest.fixture()
    def navigate_to_login_page(self):
        self.app_page.wait_for_app_page_url_change()
        self.app_page.navigate_to_login_page()

    @pytest.fixture()
    def clear_input_fields_teardown(self):
        yield
        self.login_page.clear_fields()

    @pytest.mark.run(order=1)
    @pytest.mark.usefixtures('navigate_to_login_page')
    def test_valid_login_and_logout(self):
        username = get_username()
        password = get_password()

        self.login_page.enter_username(username)
        self.login_page.enter_password(password)
        self.login_page.click_login_btn()
        self.dashboard_page.wait_for_spinner_to_disappear()

        result1 = self.dashboard_page.verify_login_successful()
        self.status.mark(result1, 'Valid login test')

        self.dashboard_page.click_logout_btn()
        result2 = self.app_page.verify_redirection_to_app_page()
        self.status.mark(result2, 'Logout after valid login test')

    @pytest.mark.run(order=2)
    @pytest.mark.usefixtures('navigate_to_login_page', 'clear_input_fields_teardown')
    def test_invalid_credentials_login(self):
        invalid_username = get_invalid_username()
        invalid_password = get_invalid_password()

        self.login_page.enter_username(invalid_username)
        self.login_page.enter_password(invalid_password)
        self.login_page.click_login_btn()

        result = self.login_page.verify_invalid_login()
        self.status.mark(result, 'Invalid credentials login test')

    @pytest.mark.run(order=3)
    @pytest.mark.usefixtures('clear_input_fields_teardown')
    def test_blank_password_login(self):
        username = get_username()

        self.login_page.enter_username(username)
        self.login_page.enter_password('')
        self.login_page.click_login_btn()

        result = self.login_page.verify_blank_password_login()
        self.status.mark(result, 'Blank password field login test')

    @pytest.mark.run(order=4)
    @pytest.mark.usefixtures('clear_input_fields_teardown')
    def test_blank_username_login(self):
        password = get_password()

        self.login_page.enter_username('')
        self.login_page.enter_password(password)
        self.login_page.click_login_btn()

        result = self.login_page.verify_blank_username_login()
        self.status.mark(result, 'Blank username field login test')

    @pytest.mark.run(order=5)
    def test_blank_username_and_password_login(self):
        self.login_page.click_login_btn()
        result = self.login_page.verify_blank_username_and_password_login()
        self.status.mark(result, 'Blank username and password fields login test')
