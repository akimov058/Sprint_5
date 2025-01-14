from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from helpers.locators import Locators
from helpers.urls import Urls

class TestConstructor:
    def test_go_click_to_bread(self, driver):
        driver.get(Urls.URL_LOGIN)

