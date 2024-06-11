from selenium import webdriver
import time
import keyboard
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome()
base_url = "http://suninjuly.github.io/redirect_accept.html"
driver.get(base_url)
driver.maximize_window()

button = driver.find_element(By.XPATH, '/html/body/form/div/div/button')
button.click()
new_window = driver.window_handles[1]
driver.switch_to.window(new_window)
time.sleep(5)
driver.quit()
