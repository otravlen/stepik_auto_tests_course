from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


try:
    site = "https://suninjuly.github.io/math.html"
    browser = webdriver.Chrome()
    browser.get(site)

    x_element = browser.find_element(By.CSS_SELECTOR, "#input_value")
    x = x_element.text
    y = calc(x)
    x_input = browser.find_element(By.CSS_SELECTOR, "#answer")
    x_input.send_keys(y)

    checkbox1 = browser.find_element(By.CSS_SELECTOR, '[for="robotCheckbox"]')
    checkbox1.click()
    radio1 = browser.find_element(By.CSS_SELECTOR, '[for="robotsRule"]')
    radio1.click()
    button1 = browser.find_element(By.CSS_SELECTOR, '.btn-default')
    button1.click()
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()