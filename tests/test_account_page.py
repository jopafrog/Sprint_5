from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators import TestLocators


class TestAccount:
    def test_enter_account_page_link_account_success(self, driver, account_page):
        name = driver.find_element(*TestLocators.NAME_INPUT).get_attribute('value')
        assert name == 'apudovkin_qa5_999'

    def test_logout_success(self, driver, account_page):
        driver.find_element(*TestLocators.LOGOUT_BUTTON).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(TestLocators.TITLE_LOGIN_PAGE))

        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/login'
