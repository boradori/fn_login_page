from pages.app_page import AppPage
from pages.login_page import LoginPage
from utilities.status import Status
import unittest
import pytest
import os
from utilities.credentials import get_username, get_password


@pytest.mark.usefixtures('class_setup')
class LoginTest(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def object_setup(self):
        self.app_page = AppPage(self.driver)
        self.login_page = LoginPage(self.driver)
        self.status = Status(self.driver)

    @pytest.mark.run(order=1)
    def test_valid_login(self):
        self.app_page.wait_for_url_change()
        self.app_page.navigate_to_login_page()
        # test username and password and login
        # logout
        print("*" * 30)
        print(get_username())
        print(get_password())
        print("*" * 30)
