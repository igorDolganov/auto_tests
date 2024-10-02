import pytest
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import *


@pytest.fixture
def driver_launch():
    options = webdriver.ChromeOptions()
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    base_url = 'https://stellarburgers.nomoreparties.site/'
    driver.get(base_url)
    driver.maximize_window()
    driver.implicitly_wait(10)
    return driver


@pytest.fixture
def login(driver_launch):
    yield
    log_email = driver_launch.find_element(*LoginPageLocators.log_email)
    log_email.send_keys('natadolganova1477@test.ru')
    log_passwd = driver_launch.find_element(*LoginPageLocators.log_passwd)
    log_passwd.send_keys('111111')
    enter = driver_launch.find_element(*RegistrationPageLocators.enter)
    enter.click()
    WebDriverWait(driver_launch, 10).until(EC.url_changes('https://stellarburgers.nomoreparties.site/'))
    current_url = driver_launch.current_url
    assert current_url  # проверка на то, что после авторизации мы попадаем на главную страницу
    driver_launch.quit()
