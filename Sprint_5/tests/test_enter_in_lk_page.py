from locators import *


class TestEnterInLkPage:
    def test_lk_page(self, driver_launch):
        personal_cabinet = driver_launch.find_element(*MainPageLocators.personal_cabinet)
        personal_cabinet.click()
