from locators import TestLocators


class TestBuilder:
    def test_buns_tab_in_builder_success(self, driver):
        driver.get('https://stellarburgers.nomoreparties.site/')

        driver.find_element(*TestLocators.SAUCES).click()
        assert 'tab_tab_type_current' not in driver.find_element(*TestLocators.BUNS).get_attribute('class')

        driver.find_element(*TestLocators.BUNS).click()
        assert 'tab_tab_type_current' in driver.find_element(*TestLocators.BUNS).get_attribute('class')

    def test_sauces_tab_in_builder_success(self, driver):
        driver.get('https://stellarburgers.nomoreparties.site/')

        assert 'tab_tab_type_current' not in driver.find_element(*TestLocators.SAUCES).get_attribute('class')

        driver.find_element(*TestLocators.SAUCES).click()
        assert 'tab_tab_type_current' in driver.find_element(*TestLocators.SAUCES).get_attribute('class')

    def test_toppings_tab_in_builder_success(self, driver):
        driver.get('https://stellarburgers.nomoreparties.site/')

        assert 'tab_tab_type_current' not in driver.find_element(*TestLocators.TOPPINGS).get_attribute('class')

        driver.find_element(*TestLocators.TOPPINGS).click()
        assert 'tab_tab_type_current' in driver.find_element(*TestLocators.TOPPINGS).get_attribute('class')
