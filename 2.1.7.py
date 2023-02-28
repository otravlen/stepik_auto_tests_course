from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from math import *
def calc(x):
    return str(log(abs(12*sin(int(x)))))


try:
    site = "http://suninjuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(site)

    val = browser.find_element(By.CSS_SELECTOR, '#input_value')
    x = calc(val.get_attribute('valuex'))
    answer = browser.find_element(By.CSS_SELECTOR, '#answer')
    answer.send_keys(x)
    check = browser.find_element(By.CSS_SELECTOR, '#robotCheckbox')
    check.click()
    sumbit = browser.find_element(By.CSS_SELECTOR, '.btn-default')
    browser.execute_script("return arguments[0].scrollIntoView(true);", sumbit)
    radio = browser.find_element(By.CSS_SELECTOR, '#robotsRule')
    radio.click()
    sumbit.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()