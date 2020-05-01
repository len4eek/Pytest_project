import pytest
from selenium.webdriver.chrome.webdriver import WebDriver
import allure
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait






def test_login(driver):


    #time.sleep(50)
    #login_button = "//button[@class='button button--green hidden__mobile margin__right_40 ng-star-inserted']"
    with allure.step("Нажали Войти"):
        WebDriverWait(driver, 100).until(EC.presence_of_element_located((By.XPATH, login_button)))
        driver.find_element_by_xpath(login_button).click()
    #login_input = "//input[@class='input__text2 not_valid ng-untouched ng-pristine ng-valid']"
    WebDriverWait(driver, 100).until(EC.presence_of_element_located((By.XPATH, login_input)))
    login_field = driver.find_element_by_xpath(login_input)
    login_field.click()
    login_field.send_keys('0991239847')
    #submit_button = "//div[@class='login__form_button']/button[@class='button button--block button--green']"
    WebDriverWait(driver, 100).until(EC.presence_of_element_located((By.XPATH, submit_button)))
    submit = driver.find_element_by_xpath(submit_button)
    submit.click()
    #password_input = "//div[@class='control__field']/input[@type = 'password']"
    WebDriverWait(driver, 100).until(EC.presence_of_element_located((By.XPATH, password_input)))
    password = driver.find_element_by_xpath(password_input)
    password.click()
    password.send_keys('Qwerty333')
    #submit_button = "//div[@class='login__form_button']/button[@class='button button--block button"
    WebDriverWait(driver, 100).until( EC.presence_of_element_located((By.XPATH, submit_button)))
    submit = driver.find_element_by_xpath(submit_button)
    submit.click()

