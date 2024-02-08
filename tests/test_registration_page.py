from random import randint
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators import TestLocators


class TestRegistration:

    def test_registration_success(self, driver):
        driver.get('https://stellarburgers.nomoreparties.site/register')

        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(TestLocators.LOGIN_PAGE_BUTTON))

        name = f'apudovkin{randint(100, 999)}'
        email = f'apudovkin_qa5_{randint(100, 999)}@yandex.ru'

        driver.find_element(*TestLocators.REGISTRATION_NAME_INPUT).send_keys(name)
        driver.find_element(*TestLocators.REGISTRATION_EMAIL_INPUT).send_keys(email)
        driver.find_element(*TestLocators.REGISTRATION_PASS_INPUT).send_keys('abc321')

        driver.find_element(*TestLocators.LOGIN_PAGE_BUTTON).click()

        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(TestLocators.PAGE_LOGIN))

        button_text = driver.find_element(*TestLocators.LOGIN_PAGE_BUTTON).text
        assert 'https://stellarburgers.nomoreparties.site/login' == driver.current_url and button_text == 'Войти'

    def test_registration_incorrect_pass_error_registration(self, driver):
        driver.get('https://stellarburgers.nomoreparties.site/register')

        driver.find_element(*TestLocators.REGISTRATION_NAME_INPUT).send_keys('apudovkin4444')
        driver.find_element(*TestLocators.REGISTRATION_EMAIL_INPUT).send_keys('apud5_4444@gamil.com')
        driver.find_element(*TestLocators.REGISTRATION_PASS_INPUT).send_keys('1')

        driver.find_element(*TestLocators.LOGIN_PAGE_BUTTON).click()

        assert driver.find_element(*TestLocators.INCORRECT_PASS_ERROR_TEXT).text == 'Некорректный пароль'
