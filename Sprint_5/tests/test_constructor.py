from locators import *


class TestsConstructor:
    def test_souce_button(self, driver_launch):
        souce_button = driver_launch.find_element(*MainPageLocators.souce_button)
        souce_button.click()
        assert ('tab_tab__1SPyG tab_tab_type_current' in souce_button.get_attribute('class'))

    def test_filling_button(self, driver_launch):
        filling_button = driver_launch.find_element(*MainPageLocators.filling_button)
        filling_button.click()
        assert ('tab_tab__1SPyG tab_tab_type_current' in filling_button.get_attribute('class'))

    def test_bread_button(self, driver_launch):
        filling_button = driver_launch.find_element(*MainPageLocators.filling_button)
        filling_button.click()
        bread_button = driver_launch.find_element(*MainPageLocators.bread_button)
        bread_button.click()
        assert ('tab_tab__1SPyG tab_tab_type_current' in bread_button.get_attribute('class'))
