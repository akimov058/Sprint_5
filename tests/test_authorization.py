from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from helpers.locators import Locators
from helpers.urls import Urls

class TestAutorization:
    def test_login_button_log_in_to_accoount_on_page_main(self,driver):
        driver.get(Urls.BASE_URL)
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((Locators.BUTTON_LOGIN_IN_ACCOUNT_MAIN_PAGE)))
        driver.find_element(*Locators.BUTTON_LOGIN_IN_ACCOUNT_MAIN_PAGE).click()
        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located((Locators.TITLE_FOR_PAGE_LOGIN)))
        driver.find_element(*Locators.EMAIL_FOR_LOGIN).send_keys('YuriAkimov17777@yandex.ru')
        driver.find_element(*Locators.PASSWORD_FOR_LOGIN).send_keys('Qwerty123')
        driver.find_element(*Locators.BUTTON_LOGIN).click()
        WebDriverWait(driver,5).until(expected_conditions.visibility_of_element_located((Locators.BUTTON_LOGIN_IN_ACCOUNT_MAIN_PAGE)))
        assert driver.current_url == Urls.BASE_URL

    def test_login_button_personal_account(self,driver):
        driver.get(Urls.BASE_URL)
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((Locators.BUTTON_LOGIN_IN_ACCOUNT_MAIN_PAGE)))
        driver.find_element(*Locators.BUTTON_PERSONAL_ACCOUNT).click()
        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located((Locators.TITLE_FOR_PAGE_LOGIN)))
        driver.find_element(*Locators.EMAIL_FOR_LOGIN).send_keys('YuriAkimov17777@yandex.ru')
        driver.find_element(*Locators.PASSWORD_FOR_LOGIN).send_keys('Qwerty123')
        driver.find_element(*Locators.BUTTON_LOGIN).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((Locators.BUTTON_LOGIN_IN_ACCOUNT_MAIN_PAGE)))
        assert driver.current_url == Urls.BASE_URL

    def test_login_button_login_on_page_register(self,driver):
        driver.get(Urls.URL_REGISTRATION)
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((Locators.BUTTON_LOGIN_ON_PAGE_LOGIN)))
        driver.find_element(*Locators.BUTTON_LOGIN_ON_PAGE_LOGIN).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((Locators.TITLE_FOR_PAGE_LOGIN)))
        driver.find_element(*Locators.EMAIL_FOR_LOGIN).send_keys('YuriAkimov17777@yandex.ru')
        driver.find_element(*Locators.PASSWORD_FOR_LOGIN).send_keys('Qwerty123')
        driver.find_element(*Locators.BUTTON_LOGIN).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((Locators.BUTTON_LOGIN_IN_ACCOUNT_MAIN_PAGE)))
        assert driver.current_url == Urls.BASE_URL

    def test_login_button_login_on_page_forgot_password(self,driver):
        driver.get(Urls.URL_FORGOT_PASSWORD)
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((Locators.BUTTON_LOGIN_ON_PAGE_LOGIN)))
        driver.find_element(*Locators.BUTTON_LOGIN_ON_PAGE_LOGIN).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((Locators.TITLE_FOR_PAGE_LOGIN)))
        driver.find_element(*Locators.EMAIL_FOR_LOGIN).send_keys('YuriAkimov17777@yandex.ru')
        driver.find_element(*Locators.PASSWORD_FOR_LOGIN).send_keys('Qwerty123')
        driver.find_element(*Locators.BUTTON_LOGIN).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((Locators.BUTTON_LOGIN_IN_ACCOUNT_MAIN_PAGE)))
        assert driver.current_url == Urls.BASE_URL