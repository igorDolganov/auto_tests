from faker import Faker
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import *


class TestsRegistration:

    def test_reg_new_user_with_correct_paswd(self, driver_launch):

        personal_cabinet = driver_launch.find_element(*MainPageLocators.personal_cabinet)
        personal_cabinet.click()
        link_registration = driver_launch.find_element(*LoginPageLocators.link_registration)
        link_registration.click()
        name = driver_launch.find_element(*RegistrationPageLocators.name)
        name.send_keys('Nata')
        random_email = driver_launch.find_element(*RegistrationPageLocators.random_email)
        fake = Faker("en_US")
        email = fake.free_email()
        random_email.send_keys(email)
        passwd = driver_launch.find_element(*RegistrationPageLocators.passwd)
        passwd.send_keys('111111')
        registration = driver_launch.find_element(*RegistrationPageLocators.registration)
        registration.click()
        WebDriverWait(driver_launch, 10).until(EC.url_contains('login'))
        current_url = driver_launch.current_url
        assert 'login' in current_url, f"Expected URL to contain 'login', but got {current_url}"
        driver_launch.quit()

    def test_reg_new_user_with_wrong_paswd(self, driver_launch):
        personal_cabinet = driver_launch.find_element(*MainPageLocators.personal_cabinet)
        personal_cabinet.click()
        link_registration = driver_launch.find_element(*LoginPageLocators.link_registration)
        link_registration.click()
        name = driver_launch.find_element(*RegistrationPageLocators.name)
        name.send_keys('Nata')
        random_email = driver_launch.find_element(*RegistrationPageLocators.random_email)
        fake = Faker("en_US")
        email = fake.free_email()
        random_email.send_keys(email)
        passwd = driver_launch.find_element(*RegistrationPageLocators.passwd)
        passwd.send_keys('11111')  # вводим короткий невалидный пароль
        registration = driver_launch.find_element(*RegistrationPageLocators.registration)
        registration.click()
        error_text = driver_launch.find_element(*RegistrationPageLocators.error_text)
        assert error_text.text == 'Некорректный пароль'
        driver_launch.quit()
