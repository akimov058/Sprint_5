from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from helpers.locators import Locators
from helpers.urls import Urls

class TestPersonalAccount:
    def test_go_click_on_personal_account(self,driver):
        driver.get(Urls.URL_LOGIN)
        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located((Locators.TITLE_FOR_PAGE_LOGIN)))
        driver.find_element(*Locators.EMAIL_FOR_LOGIN).send_keys('YuriAkimov17777@yandex.ru')
        driver.find_element(*Locators.PASSWORD_FOR_LOGIN).send_keys('Qwerty123')
        driver.find_element(*Locators.BUTTON_LOGIN).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((Locators.BUTTON_PERSONAL_ACCOUNT)))
        driver.find_element(*Locators.BUTTON_PERSONAL_ACCOUNT).click()
        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located((Locators.BUTTON_PROFILE)))
        assert driver.current_url == Urls.URL_PERSONAL_ACCOUNT

    def test_go_click_on_constructor(self,driver):
        driver.get(Urls.URL_LOGIN)
        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located((Locators.TITLE_FOR_PAGE_LOGIN)))
        driver.find_element(*Locators.EMAIL_FOR_LOGIN).send_keys('YuriAkimov17777@yandex.ru')
        driver.find_element(*Locators.PASSWORD_FOR_LOGIN).send_keys('Qwerty123')
        driver.find_element(*Locators.BUTTON_LOGIN).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((Locators.BUTTON_PERSONAL_ACCOUNT)))
        driver.find_element(*Locators.BUTTON_PERSONAL_ACCOUNT).click()
        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located((Locators.BUTTON_PROFILE)))
        driver.find_element(*Locators.BUTTON_CONSTRUCTOR).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((Locators.BUTTON_LOGIN_IN_ACCOUNT_MAIN_PAGE)))
        assert driver.current_url == Urls.BASE_URL

    def test_go_click_on_logo(self,driver):
        driver.get(Urls.URL_LOGIN)
        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located((Locators.TITLE_FOR_PAGE_LOGIN)))
        driver.find_element(*Locators.EMAIL_FOR_LOGIN).send_keys('YuriAkimov17777@yandex.ru')
        driver.find_element(*Locators.PASSWORD_FOR_LOGIN).send_keys('Qwerty123')
        driver.find_element(*Locators.BUTTON_LOGIN).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((Locators.BUTTON_PERSONAL_ACCOUNT)))
        driver.find_element(*Locators.BUTTON_PERSONAL_ACCOUNT).click()
        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located((Locators.BUTTON_PROFILE)))
        driver.find_element(*Locators.BUTTON_LOGO).click()
        assert driver.current_url == Urls.BASE_URL