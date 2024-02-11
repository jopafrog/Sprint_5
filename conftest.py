import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators import TestLocators


@pytest.fixture(scope='function')
def driver():
    options = Options()
    options.add_argument('--window-size=1920,1080')
    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()


@pytest.fixture(scope='function')
def account_page(driver):
    driver.get('https://stellarburgers.nomoreparties.site/login')

    driver.find_element(*TestLocators.EMAIL_INPUT).send_keys('apud_qa5_999@yandex.ru')
    driver.find_element(*TestLocators.PASS_INPUT).send_keys('qwe321')

    driver.find_element(*TestLocators.LOGIN_PAGE_BUTTON).click()
    WebDriverWait(driver, 3).until(
        expected_conditions.visibility_of_element_located(TestLocators.LOGIN_BUTTON_ON_MAIN_PAGE))

    driver.find_element(*TestLocators.ACCOUNT_PAGE_LINK).click()

    WebDriverWait(driver, 3).until(
        expected_conditions.visibility_of_element_located(TestLocators.NAME_INPUT))

    yield account_page
