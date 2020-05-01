from BaseApp import BasePage
from selenium.webdriver.common.by import By

class LoginLocators:

    Locator_login_button = (By.XPATH, "//button[@class='button button--green hidden__mobile margin__right_40 ng-star-inserted']")
    Locator_login_input = (By.XPATH, "//input[@class='input__text2 not_valid ng-untouched ng-pristine ng-valid']")
    Locator_submit_button = (By.XPATH, "//div[@class='login__form_button']/button[@class='button button--block button--green']")
    Locator_password_input = (By.XPATH, "//div[@class='control__field']/input[@type = 'password']")
    Locator_username = (By.XPATH, "//div[@class='profile__name-block']")

class LogIn(BasePage):

    def login_form(self):
        login_button = self.find_element(LoginLocators.Locator_login_button)
        login_button.click()
        return login_button

    def submit_login(self, login, password):
        submit_login = self.find_element(LoginLocators.Locator_login_input)
        submit_login.click()
        submit_login.send_keys(login)
        click_submit = self.find_element(LoginLocators.Locator_submit_button)
        click_submit.click()
        submit_password = self.find_element(LoginLocators.Locator_password_input)
        submit_password.click()
        submit_password.send_keys(password)
        click_submit = self.find_element(LoginLocators.Locator_submit_button)
        click_submit.click()

    def profile_name(self):
        profile_name = self.find_element(LoginLocators.Locator_username)
        return profile_name
