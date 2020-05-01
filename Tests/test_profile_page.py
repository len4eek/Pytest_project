from Pages.ProfilePage import ProfilePage
from Pages.ProfilePage import Locator
import Tests.test_login

def test_profile_page(browser):

    profile = ProfilePage(browser)

    Tests.test_login.test_autorization(browser)

    profile.click_profile_button()
    profile.click_setting_button()

    # russian
    profile.select_RU()

    assert profile.profile_title().text == "Мой профиль"

    #image = driver.find_element_by_xpath("//app-profile-page/div[2]/div/div[1]/div/img")
    # image.click()
    # load_image = driver.find_element_by_xpath("//p[@id='load']")
    # load_image.click()п
    # добавить загрузку картинки профиля

    assert profile.client_title().text == "Name LastName"

    assert profile.status_title().text == "Статус"

    assert profile.account_title().text == "Активный"

    assert profile.client_status_title().text == "Клиент Сбербанка"

    #смена тарифа
    #tariff = "//div[@class='profile__item_subtitle'][1]"
    #WebDriverWait(driver, 100).until(EC.element_to_be_clickable((By.XPATH, tariff)))
    #tariff_button = driver.find_element_by_xpath(tariff)
    #tariff_button.click()


