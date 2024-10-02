from locators import *


class TestsLogin:
    def test_enter_in_account_main(self, driver_launch, login):
        enter_button = driver_launch.find_element(*MainPageLocators.enter_button)
        enter_button.click()  # после этого кода в дело вступает фикстура login и совершает авторизацию

    def test_enter_in_account_profile(self, driver_launch, login):
        personal_cabinet = driver_launch.find_element(*MainPageLocators.personal_cabinet)
        personal_cabinet.click()

    def test_enter_in_account_through_registration(self, driver_launch, login):
        personal_cabinet = driver_launch.find_element(*MainPageLocators.personal_cabinet)
        personal_cabinet.click()
        link_registration = driver_launch.find_element(*LoginPageLocators.link_registration)
        link_registration.click()
        enter_in_account = driver_launch.find_element(*RegistrationPageLocators.enter_in_account)
        enter_in_account.click()

    def test_enter_in_account_through_recovery_passwd(self, driver_launch, login):
        personal_cabinet = driver_launch.find_element(*MainPageLocators.personal_cabinet)
        personal_cabinet.click()
        recovery_button = driver_launch.find_element(*LoginPageLocators.recovery_button)
        recovery_button.click()
        remember_button_enter = driver_launch.find_element(*RecoveryPageLocators.remember_button_enter)
        remember_button_enter.click()
