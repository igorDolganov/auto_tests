from locators import *


class TestsLinkConstructor:
    def test_constructor_button(self, driver_launch):
        personal_cabinet = driver_launch.find_element(*MainPageLocators.personal_cabinet)
        personal_cabinet.click()
        constructor_button = driver_launch.find_element(*MainPageLocators.constructor_button)
        constructor_button.click()
        current_url = driver_launch.current_url
        assert current_url
        driver_launch.quit()

    def test_logo_button(self, driver_launch):
        personal_cabinet = driver_launch.find_element(*MainPageLocators.personal_cabinet)
        personal_cabinet.click()
        logo_button = driver_launch.find_element(*MainPageLocators.logo_button)
        logo_button.click()
        current_url = driver_launch.current_url
        assert current_url
        driver_launch.quit()
