from selenium.webdriver.common.by import By
import time
from BaseApp import BasePage

class Locator:

    Locator_profile_button = (By.XPATH, "//div[@class='profile__preview_photo ng-star-inserted']")
    Locator_profile_setting = (By.XPATH, "//a[@href='#/profile']")
    Locator_RU_language_button = (By.XPATH, "//a[@class='footer__menu_item footer__menu_item_lang ng-star-inserted' and text()='Рус']")
    Locator_profile_title = (By.XPATH, "//div[@class='profile__title']")
    Locator_client_name = (By.XPATH, "//div[@class='profile__info_title ng-star-inserted']")
    Locator_status_title = (By.XPATH, "//div[@class='profile__personal_title'][1]")
    Locator_account_status = (By.XPATH, "//div[@class='personal__card cs-profile-50-pers'][1]/div[@class='personal__card_status']")
    Locator_client_status = (By.XPATH, "//div[@class='personal__card cs-profile-50-pers'][2]/div[@class='personal__card_status']")

class ProfilePage(BasePage):

    def click_profile_button(self):
        click_button = self.find_element(Locator.Locator_profile_button)
        time.sleep(10)
        click_button.click()
        return click_button

    def click_setting_button(self):
        time.sleep(10)
        click_button1 = self.find_element(Locator.Locator_profile_setting)
        click_button1.click()
        return click_button1

    def select_RU(self):
        select_RU = self.find_element(Locator.Locator_RU_language_button)
        select_RU.click()
        return select_RU

    def profile_title(self):
        profile_title = self.find_element(Locator.Locator_profile_title)
        return profile_title

    def client_title(self):
        client_title = self.find_element(Locator.Locator_client_name)
        return client_title

    def status_title(self):
        status_title = self.find_element(Locator.Locator_status_title)
        return status_title

    def account_title(self):
        account_title = self.find_element(Locator.Locator_account_status)
        return account_title

    def client_status_title(self):
        client_status_title = self.find_element(Locator.Locator_client_status)
        return client_status_title
