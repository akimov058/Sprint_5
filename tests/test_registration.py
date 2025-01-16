from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from helpers.locators import Locators
from helpers.urls import Urls
from helpers.data import Data

class TestRegistration:
    def test_registration_success(self,driver):
        driver.get(Urls.URL_REGISTRATION)
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((Locators.NAME_FOR_REGISTRATION)))
        driver.find_element(*Locators.NAME_FOR_REGISTRATION).send_keys('Юрий')
        driver.find_element(*Locators.EMAIL_FOR_REGISTARTION).send_keys(Data.create_new_email_for_registration())
        driver.find_element(*Locators.PASSWORD_FOR_REGISTRATION).send_keys(Data.create_new_password_for_registration())
        driver.find_element(*Locators.BUTTON_FOR_REGISTRATION).click()
        WebDriverWait(driver,5).until(expected_conditions.visibility_of_element_located((Locators.TITLE_FOR_PAGE_LOGIN)))
        assert driver.current_url == Urls.URL_LOGIN

    def test_registration_incorrect_password(self,driver):
        driver.get(Urls.URL_REGISTRATION)
        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located((Locators.NAME_FOR_REGISTRATION)))
        driver.find_element(*Locators.NAME_FOR_REGISTRATION).send_keys('Юрий')
        driver.find_element(*Locators.EMAIL_FOR_REGISTARTION).send_keys(Data.create_new_email_for_registration())
        driver.find_element(*Locators.PASSWORD_FOR_REGISTRATION).send_keys('123')
        driver.find_element(*Locators.BUTTON_FOR_REGISTRATION).click()
        WebDriverWait(driver,5).until(expected_conditions.visibility_of_element_located((Locators.ERROR_FOR_INCORRECT_PASSWORD)))
        assert driver.find_element(*Locators.ERROR_FOR_INCORRECT_PASSWORD).text == 'Некорректный пароль'









