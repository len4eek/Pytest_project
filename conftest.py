import pytest
from selenium.webdriver.chrome.webdriver import WebDriver


@pytest.fixture(scope="session")
def browser():
    path = '/Users/elenazhuchenko/PycharmProjects/test.py/Drivers/chromedriver'
    driver = WebDriver(executable_path=path)
    yield driver
    driver.close()
    driver.quit()
