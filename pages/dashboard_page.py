from selenium.webdriver.common.by import By
from base.selenium_driver import SeleniumDriver


class DashboardPage(SeleniumDriver):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # locators
    _spinner = (By.XPATH, "//div[@class='preloader']/div[contains(text(),'Processing')]")
    _welcome_msg = (By.XPATH, "//h1[contains(., 'Welcome')]")
    _fiscal_note_logo = (By.XPATH, "//img[@alt='FiscalNote' and @width='80']")
    _side_bar_footer = (By.CSS_SELECTOR, "div[class='sidebar-footer']")
    _account_menu = (By.CSS_SELECTOR, "#ember1321")
    _hovered_settings_btn = (By.CSS_SELECTOR, "div[class='ember-view sidebar-elem force-hover']")
    _logout_btn = (By.CSS_SELECTOR, "a[class='logout']:nth-child(1)")

    def wait_for_spinner_to_disappear(self):
        self.wait_for_element(self._spinner, False)

    def verify_login_successful(self):
        welcome_msg = self.wait_for_element(self._welcome_msg)
        return self.is_element_present(None, welcome_msg)

    def click_logout_btn(self):
        side_bar_footer = self.wait_for_element(self._side_bar_footer)
        self.move_to_element(side_bar_footer)

        account_menu = self.wait_for_element(self._account_menu)
        self.move_to_element(account_menu)

        self.wait_for_element(self._hovered_settings_btn)
        self.click_element(self._logout_btn)
