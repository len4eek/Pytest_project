from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.base_url = 'http://dev1.itstudiodev.com:8080/#/'

    def find_element(self, locator, time=30):
        return WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator),
                                                      message="Can't find element by locator {locator}")

    def find_elements(self, locator, time=30):
        return WebDriverWait(self.driver, time).until(EC.presence_of_all_element_located(locator),
                                                      message="Can't find elements by locator {locator}")

    def go_to_site(self):
        return self.driver.get(self.base_url)
