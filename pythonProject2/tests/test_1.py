import time

from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.login_page import LoginPage


class Test1():
    def test_select_product(self):
        driver = webdriver.Chrome(ChromeDriverManager().install())
        base_url = 'https://www.saucedemo.com/'
        driver.get(base_url)
        driver.maximize_window()


        login_standard_user = 'standard_user'
        password_all = 'secret_sauce'

        login = LoginPage(driver)
        login.authorization(login_standard_user, password_all)

        select_product = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[@id = 'add-to-cart-sauce-labs-backpack']")))
        select_product.click()

        enter_shopping_cart = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@id = 'shopping_cart_container']")))
        enter_shopping_cart.click()

        success_test = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[@class = 'title']")))
        value_success_test = success_test.text
        assert value_success_test == 'Your Cart'
        time.sleep(5)


Test1()

