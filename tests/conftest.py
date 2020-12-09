import pytest
from base.webdriverfactory import WebDriverFactory


def pytest_addoption(parser):
    parser.addoption('--browser')


@pytest.fixture(scope='function')
def setup():
    print('Running method level setup')
    yield
    print('Running method level teardown')


@pytest.fixture(scope='class')
def class_setup(request):
    print('Running class_setup')

    browser = request.config.getoption('--browser')

    wdf = WebDriverFactory(browser)
    driver = wdf.get_webdriver()

    if request.cls is not None:
        request.cls.driver = driver
        request.cls.browser = browser

    yield driver
    driver.quit()
    print('Running class_teardown')
