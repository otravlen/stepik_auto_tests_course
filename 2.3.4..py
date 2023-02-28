from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from math import *


def calc(x):
    return str(log(abs(12*sin(int(x)))))


try:
    site = "http://suninjuly.github.io/alert_accept.html"
    browser = webdriver.Chrome()
    browser.get(site)
    time.sleep(1)
    sumbit = browser.find_element(By.CSS_SELECTOR, '.btn')
    sumbit.click()
    time.sleep(1)
    alert = browser.switch_to.alert
    alert.accept()
    time.sleep(1)
    x = browser.find_element(By.CSS_SELECTOR, '#input_value')
    x1 = x.text
    print(x1)
    answer = browser.find_element(By.CSS_SELECTOR, '#answer')
    answer.send_keys(calc(x1))
    sumbit1 = browser.find_element(By.CSS_SELECTOR, '.btn-primary')
    sumbit1.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()