from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import pytest
from selenium.webdriver.support.ui import Select



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

def test_dropdown():
    driver.get(base_url)
    login = driver.find_element(By.ID, 'user-name')
    login.send_keys('standard_user')
    password = driver.find_element(By.ID, 'password')
    password.send_keys('secret_sauce')
    login_button = driver.find_element(By.ID, 'login-button')
    login_button.click()
    name1 = driver.find_element(By.XPATH, "//div[text()='Sauce Labs Backpack']")
    assert name1.text == 'Sauce Labs Backpack'
    dropdown = Select(driver.find_element(By.CLASS_NAME, "product_sort_container"))
    dropdown.select_by_index(1)
    name2 = driver.find_element(By.XPATH, "//div[text()='Test.allTheThings() T-Shirt (Red)']")
    assert name2.text == 'Test.allTheThings() T-Shirt (Red)'
    driver.quit()


def test_buy():
    driver.get(base_url)
    login = driver.find_element(By.ID, 'user-name')
    login.send_keys('standard_user')
    password = driver.find_element(By.ID, 'password')
    password.send_keys('secret_sauce')
    login_button = driver.find_element(By.ID, 'login-button')
    login_button.click()
    add_cart_button1 = driver.find_element(By.ID, 'add-to-cart-sauce-labs-backpack')
    add_cart_button1.click()
    cart = driver.find_element(By.CLASS_NAME, 'shopping_cart_link')
    cart.click()
    checkout = driver.find_element(By. ID, 'checkout')
    checkout.click()
    first_name = driver.find_element(By.ID, 'first-name')
    first_name.send_keys('first_name')
    last_name = driver.find_element(By.ID, 'last-name')
    last_name.send_keys('last name')
    post_code = driver.find_element(By.ID, 'postal-code')
    post_code.send_keys('111111')
    cont_button = driver.find_element(By.ID, 'continue')
    cont_button.click()
    finish_button = driver.find_element(By.ID, 'finish')
    finish_button.click()
    complete = driver.find_element(By.CLASS_NAME, 'complete-header')
    assert complete.text == 'Thank you for your order!'
    driver.quit()
