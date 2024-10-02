from selenium.webdriver.common.by import By


class MainPageLocators:
    personal_cabinet = (By.XPATH, '//p[text()="Личный Кабинет"]')
    souce_button = (By.XPATH, '(//div[contains(@class,"tab_tab__1SPyG ")])[2]')
    filling_button = (By.XPATH, '(//div[contains(@class,"tab_tab__1SPyG ")])[3]')
    bread_button = (By.XPATH, '//div[contains(@class,"tab_tab__1SPyG ")]')
    enter_button = (By.XPATH, '//button[text()="Войти в аккаунт"]')
    constructor_button = (By.XPATH, '//p[text()="Конструктор"]')
    logo_button = (By.XPATH, '//*[@id="root"]/div/header/nav/div/a')


class RegistrationPageLocators:
    random_email = (By.XPATH, '(//input[@name="name"])[2]')
    passwd = (By.NAME, 'Пароль')
    enter = (By.XPATH, '//button[text()="Войти"]')
    enter_in_account = (By.XPATH, '//a[@href="/login"]')
    name = (By.XPATH, '//input[@name="name"]')
    registration = (By.XPATH, '//button[text()="Зарегистрироваться"]')
    error_text = (By.XPATH, '//p[text()="Некорректный пароль"]')


class LoginPageLocators:
    log_email = (By.NAME, 'name')
    log_passwd = (By.NAME, 'Пароль')
    enter_login = (By.XPATH, '//button[text()="Войти"]')
    link_registration = (By.XPATH, '//a[@class="Auth_link__1fOlj"]')
    recovery_button = (By.XPATH, '//a[@href="/forgot-password"]')


class ProfileLocators:
    exit_button = (By.XPATH, '//button[text()="Выход"]')


class RecoveryPageLocators:
    remember_button_enter = (By.XPATH, '//a[@href="/login"]')



