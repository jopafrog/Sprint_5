from selenium.webdriver.common.by import By


class TestLocators:
    # Поля формы регистрации
    REGISTRATION_NAME_INPUT = By.XPATH, './/label[text()="Имя"]/parent::div/input'
    REGISTRATION_EMAIL_INPUT = By.XPATH, './/label[text()="Email"]/parent::div/input'
    REGISTRATION_PASS_INPUT = By.XPATH, './/label[text()="Пароль"]/parent::div/input'
    # REGISTRATION_BUTTON = By.XPATH, './/button[contains(@class, "button_button_size_medium")]'  # Кнопка регистрации

    LOGIN_EMAIL = By.XPATH, './/label[text()="Email"]/parent::div/input'
    LOGIN_PASS = By.XPATH, './/label[text()="Пароль"]/parent::div/input'
    LOGIN_PAGE_BUTTON = By.XPATH, './/button[contains(@class, "button_button_size_medium")]'
    LOGIN_IN_REGISTRATION_PAGE = By.LINK_TEXT, 'Войти'

    PAGE_LOGIN = By.XPATH, './/h2[text()="Вход"]'

    ACCOUNT_PAGE_BUTTON = By.LINK_TEXT, 'Личный Кабинет'

    INCORRECT_PASS_ERROR_TEXT = By.XPATH, './/p[contains(@class, "input__error")]'

    LOGIN_BUTTON_ON_MAIN_PAGE = By.XPATH, './/button[contains(@class, "button_button_size_large")]'

    # TITLE_MAIN_PAGE = By.XPATH, './/h1[text()="Соберите бургер"]'
    # PLACE_ORDER_BUTTON_ON_MAIN_PAGE = By.XPATH, './/button[text()="Оформить заказ"]'
