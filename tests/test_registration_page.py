import time
from locators import TestLocators


class TestRegistration:

    def test_registration_success(self, driver):
        driver.get(TestLocators.SITE)
        time.sleep(2)

        driver.quit()
