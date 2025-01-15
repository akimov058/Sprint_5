from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from helpers.locators import Locators
from helpers.urls import Urls

class TestConstructor:
    def test_go_click_to_sauce(self, driver):
        driver.get(Urls.BASE_URL)
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((Locators.SECTION_BREAD)))
        driver.find_element(*Locators.SECTION_BREAD).click()
        assert driver.find_element(*Locators.UL_SECTION_SAUCE).is_displayed()

    def test_go_click_to_bread(self, driver):
        driver.get(Urls.BASE_URL)
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((Locators.SECTION_BREAD)))
        driver.find_element(*Locators.SECTION_BREAD).click()
        assert driver.find_element(*Locators.UL_SECTION_DREAD).is_displayed()

    def test_go_click_to_filling(self, driver):
        driver.get(Urls.BASE_URL)
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((Locators.SECTION_BREAD)))
        driver.find_element(*Locators.SECTION_FILLING).click()
        assert driver.find_element(*Locators.UL_SECTION_FILLING).is_displayed()

