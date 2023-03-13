import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pytest

class TestAbs(unittest.TestCase):
    def test_registration1(self):
        self.site = "http://suninjuly.github.io/registration1.html"
        self.browser = webdriver.Chrome()
        self.browser.get(self.site)
        self.fname = self.browser.find_element(By.CSS_SELECTOR, "[placeholder='Input your first name']")
        self.fname.send_keys('Наталья')
        self.lname = self.browser.find_element(By.CSS_SELECTOR, "[placeholder='Input your last name']")
        self.lname.send_keys('Морская Пехота')
        self.email = self.browser.find_element(By.CSS_SELECTOR, "[placeholder='Input your email']")
        self.email.send_keys('pehota@mail.com')
        self.phone = self.browser.find_element(By.CSS_SELECTOR, "[placeholder='Input your phone:']")
        self.phone.send_keys('89309840329')
        self.adres = self.browser.find_element(By.CSS_SELECTOR, "[placeholder='Input your address:']")
        self.adres.send_keys('sdlf;dsf;ds')
        self.sumbit = self.browser.find_element(By.CSS_SELECTOR, '.btn-default')
        self.sumbit.click()
        self.congratulations = self.browser.find_element(By.XPATH, '//h1')
        self.assertEqual(self.congratulations.text, 'Congratulations! You have successfully registered!', 'wrong text')
        # ожидание чтобы визуально оценить результаты прохождения скрипта
        time.sleep(3)
        # закрываем браузер после всех манипуляций
        self.browser.quit()

    def test_registration2(self):
        self.site = "http://suninjuly.github.io/registration2.html"
        self.browser = webdriver.Chrome()
        self.browser.get(self.site)
        self.fname = self.browser.find_element(By.CSS_SELECTOR, "[placeholder='Input your first name']")
        self.fname.send_keys('Наталья')
        self.lname = self.browser.find_element(By.CSS_SELECTOR, "[placeholder='Input your last name']")
        self.lname.send_keys('Морская Пехота')
        self.email = self.browser.find_element(By.CSS_SELECTOR, "[placeholder='Input your email']")
        self.email.send_keys('pehota@mail.com')
        self.phone = self.browser.find_element(By.CSS_SELECTOR, "[placeholder='Input your phone:']")
        self.phone.send_keys('89309840329')
        self.adres = self.browser.find_element(By.CSS_SELECTOR, "[placeholder='Input your address:']")
        self.adres.send_keys('sdlf;dsf;ds')
        self.sumbit = self.browser.find_element(By.CSS_SELECTOR, '.btn-default')
        self.sumbit.click()
        self.congratulations = self.browser.find_element(By.XPATH, '//h1')
        self.assertEqual(self.congratulations.text, 'Congratulations! You have successfully registered!', 'wrong text')
        # ожидание чтобы визуально оценить результаты прохождения скрипта
        time.sleep(3)
        # закрываем браузер после всех манипуляций
        self.browser.quit()



if __name__ == "__main__":
    pytest.main()
