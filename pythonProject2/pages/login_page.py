
# from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base


class LoginPage(Base):

    url = 'https://www.saucedemo.com/'
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver


    # Locators

    user_name = '//input[@id="user-name"]'
    password = '//input[@id="password"]'
    button_login = '//input[@id="login-button"]'

    # Getters

    def get_user_name(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.user_name)))

    def get_password(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.password)))

    def get_button_login(self):
        # return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.button_login)))


    # Actions

    def input_user_name(self, username):
        self.get_user_name().send_keys(username)
        print("Input user name")

    def input_password(self, password):
        self.get_password().send_keys(password)
        print("Input password")

    def input_button_login(self, button_login):
        self.get_button_login().send_keys(button_login)
        print("Click button")


    # Функция авторизации на сайте

    def authorization(self, login_name, login_password):

        user_name = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//input[@id="user-name"]')))
        user_name.send_keys(login_name)
        password = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//input[@id="password"]')))
        password.send_keys(login_password)

        button_login = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//input[@id="login-button"]')))
        button_login.click()
        