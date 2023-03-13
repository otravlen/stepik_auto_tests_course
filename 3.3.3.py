from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pytest





def test_registration1():
    site = "http://suninjuly.github.io/registration1.html"
    browser = webdriver.Chrome()
    browser.get(site)
    fname = browser.find_element(By.CSS_SELECTOR, "[placeholder='Input your first name']")
    fname.send_keys('Наталья')
    lname = browser.find_element(By.CSS_SELECTOR, "[placeholder='Input your last name']")
    lname.send_keys('Морская Пехота')
    email = browser.find_element(By.CSS_SELECTOR, "[placeholder='Input your email']")
    email.send_keys('pehota@mail.com')
    phone = browser.find_element(By.CSS_SELECTOR, "[placeholder='Input your phone:']")
    phone.send_keys('89309840329')
    adres = browser.find_element(By.CSS_SELECTOR, "[placeholder='Input your address:']")
    adres.send_keys('sdlf;dsf;ds')
    sumbit = browser.find_element(By.CSS_SELECTOR, '.btn-default')
    sumbit.click()
    congratulations = browser.find_element(By.XPATH, '//h1')
    assert(congratulations.text, 'Congratulations! You have successfully registered!', 'wrong text')
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(3)
    # закрываем браузер после всех манипуляций
    browser.quit()


def test_registration2(self):
    site = "http://suninjuly.github.io/registration2.html"
    browser = webdriver.Chrome()
    browser.get(site)
    fname = browser.find_element(By.CSS_SELECTOR, "[placeholder='Input your first name']")
    fname.send_keys('Наталья')
    lname = browser.find_element(By.CSS_SELECTOR, "[placeholder='Input your last name']")
    lname.send_keys('Морская Пехота')
    email = browser.find_element(By.CSS_SELECTOR, "[placeholder='Input your email']")
    email.send_keys('pehota@mail.com')
    phone = browser.find_element(By.CSS_SELECTOR, "[placeholder='Input your phone:']")
    phone.send_keys('89309840329')
    adres = browser.find_element(By.CSS_SELECTOR, "[placeholder='Input your address:']")
    adres.send_keys('sdlf;dsf;ds')
    sumbit = browser.find_element(By.CSS_SELECTOR, '.btn-default')
    sumbit.click()
    congratulations = browser.find_element(By.XPATH, '//h1')
    assert (congratulations.text, 'Congratulations! You have successfully registered!', 'wrong text')
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(3)
    # закрываем браузер после всех манипуляций
    browser.quit()

if __name__ == '__main__':
    pytest.main()