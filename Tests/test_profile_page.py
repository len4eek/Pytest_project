import pytest
from selenium.webdriver.chrome.webdriver import WebDriver
import allure
from Tests import test_login
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


@pytest.fixture
def driver(request):
    path = '/Users/elenazhuchenko/PycharmProjects/test.py/Drivers/chromedriver'
    c_driver = WebDriver(executable_path=path)
    with allure.step("Открыли сайт"):
        c_driver.get('http://dev1.itstudiodev.com:8080/#/')
    yield c_driver
    with allure.step("Закрыли сайт"):
        c_driver.close()
        c_driver.quit()


def test_profile_page(driver):
    test_login.test_login(driver)

    profile_button = "//div[@class='profile__preview_photo ng-star-inserted']"

    try:
        WebDriverWait(driver, 100).until(
            EC.presence_of_element_located((By.XPATH, profile_button))
        )
    finally:
        submit = driver.find_element_by_xpath(profile_button)
        submit.click()

    profile_setting = "//a[@href='#/profile']"

    try:
        WebDriverWait(driver, 100).until(
            EC.presence_of_element_located((By.XPATH, profile_setting))
        )
    finally:
        submit1 = driver.find_element_by_xpath(profile_setting)
        submit1.click()

    # russian
    language_button = "//a[@class='footer__menu_item footer__menu_item_lang ng-star-inserted' and text()='Рус']"
    try:
        WebDriverWait(driver, 100).until(
            EC.presence_of_element_located((By.XPATH, language_button))
        )
    finally:
        language_button = driver.find_element_by_xpath(language_button)
        language_button.click()
    title = driver.find_element_by_xpath("//div[@class='profile__title']")
    assert title.text == "Мой профиль"

    image = driver.find_element_by_xpath("//app-profile-page/div[2]/div/div[1]/div/img")
    # image.click()
    # load_image = driver.find_element_by_xpath("//p[@id='load']")
    # load_image.click()
    # добавить загрузку картинки профиля

    client_name = driver.find_element_by_xpath("//div[@class='profile__info_title ng-star-inserted']")
    assert client_name.text == "Name LastName"

    status_title = driver.find_element_by_xpath("//div[@class='profile__personal_title'][1]")
    assert status_title.text == "Статус"

    account_status = driver.find_element_by_xpath("//div[@class='personal__card cs-profile-50-pers'][1]/div[@class='personal__card_status']")
    assert account_status.text == "Активный"

    client_status = driver.find_element_by_xpath("//div[@class='personal__card cs-profile-50-pers'][2]/div[@class='personal__card_status']")
    assert client_status.text == "Клиент Сбербанка"

    #смена тарифа
    tariff = "//div[@class='profile__item_subtitle'][1]"
    WebDriverWait(driver, 100).until(EC.element_to_be_clickable((By.XPATH, tariff)))
    tariff_button = driver.find_element_by_xpath(tariff)
    #tariff_button.click()


