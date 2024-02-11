from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators import TestLocators


class TestAccount:
    def test_enter_account_page_link_account_success(self, driver, account_page):
        name = driver.find_element(*TestLocators.NAME_INPUT).get_attribute('value')
        assert name == 'apudovkin_qa5_999'
