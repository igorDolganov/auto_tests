from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest

driver = webdriver.Chrome(ChromeDriverManager().install())
base_url = 'https://www.saucedemo.com/'
driver.get(base_url)


def test_remove():
    login = driver.find_element(By.ID, 'user-name')
    login.send_keys('standard_user')
    password = driver.find_element(By.ID, 'password')
    password.send_keys('secret_sauce')
    login_button = driver.find_element(By.ID, 'login-button')
    login_button.click()
    add_cart_button = driver.find_element(By. ID, 'add-to-cart-sauce-labs-backpack')
    add_cart_button.click()
    remove_cart_button = driver.find_element(By. ID,'remove-sauce-labs-backpack')
    assert remove_cart_button.text == 'Remove'
    remove_cart_button.click()
    add_cart_button1 = driver.find_element(By.ID, 'add-to-cart-sauce-labs-backpack')
    assert add_cart_button1.text == 'Add to cart'
    driver.quit()
