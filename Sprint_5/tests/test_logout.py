from locators import *
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestLogout:
    def test_logout(self, driver_launch):
        enter_button = driver_launch.find_element(*MainPageLocators.enter_button)
        enter_button.click()
        log_email = driver_launch.find_element(*LoginPageLocators.log_email)
        log_email.send_keys('natadolganova1477@test.ru')
        log_passwd = driver_launch.find_element(*LoginPageLocators.log_passwd)
        log_passwd.send_keys('111111')
        enter_login = driver_launch.find_element(*LoginPageLocators.enter_login)
        enter_login.click()
        personal_cabinet = driver_launch.find_element(*MainPageLocators.personal_cabinet)
        personal_cabinet.click()
        exit_button = driver_launch.find_element(*ProfileLocators.exit_button)
        exit_button.click()
        WebDriverWait(driver_launch, 10).until(EC.url_contains('login'))
        current_url = driver_launch.current_url
        assert 'login' in current_url, f"Expected URL to contain 'login', but got {current_url}"
        driver_launch.quit()
