from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from helpers.locators import Locators
from helpers.urls import Urls

class TestPersonalAccount:
    def test_log_out(self,driver):
        driver.get(Urls.URL_LOGIN)
        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located((Locators.TITLE_FOR_PAGE_LOGIN)))
        driver.find_element(*Locators.EMAIL_FOR_LOGIN).send_keys('YuriAkimov17777@yandex.ru')
        driver.find_element(*Locators.PASSWORD_FOR_LOGIN).send_keys('Qwerty123')
        driver.find_element(*Locators.BUTTON_LOGIN).click()
        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located((Locators.BUTTON_PERSONAL_ACCOUNT)))
        driver.find_element(*Locators.BUTTON_PERSONAL_ACCOUNT).click()
        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located((Locators.BUTTON_LOG_OUT)))
        driver.find_element(*Locators.BUTTON_LOG_OUT).click()
        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located((Locators.TITLE_FOR_PAGE_LOGIN)))
        assert driver.current_url == Urls.URL_LOGIN