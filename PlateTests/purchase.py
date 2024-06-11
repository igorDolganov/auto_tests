import time
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.common.by import By



class Test1():
    def test_food(self):
        driver = webdriver.Chrome(ChromeDriverManager().install())
        base_url = 'https://tarelka.in-aim.dev/'
        driver.get(base_url)
        driver.maximize_window()

        # авторизация постоянного юзера
        driver.implicitly_wait(10)
        login = driver.find_element(By.XPATH, "//a[@class='btn btn-dark']")
        login.click()

        # ввод телефона
        telephone = driver.find_element(By.NAME, "telephone")
        telephone.click()
        telephone.send_keys('9999999999')

        # получаем код из алерта
        driver.find_element(By.XPATH, "//button[text()='Получить код']").click()
        time.sleep(1)
        alert = driver.find_element(By.XPATH, '//*[@id="app"]/div[1]')
        number = alert.text

        # ввод кода
        code = driver.find_element(By.XPATH, "//input[@inputmode='numeric']")
        code.send_keys(number)
        driver.find_element(By.XPATH, "(//div[@class='login-page__field'])[3]").click()
        time.sleep(1)


