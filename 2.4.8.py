from selenium.webdriver.common.by import By
from selenium.webdriver.support.expected_conditions import text_to_be_present_in_element
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from time import sleep
from math import *


def calc(x):
    return str(log(abs(12*sin(int(x)))))


try:
    site = "http://suninjuly.github.io/explicit_wait2.html"
    browser = webdriver.Chrome()
    browser.get(site)
    wait = WebDriverWait(browser, 10)
    element = wait.until(EC.text_to_be_present_in_element((By.ID, 'price'), '100'))
    button = browser.find_element(By.ID, 'book')
    button.click()
    x = browser.find_element(By.CSS_SELECTOR, '#input_value').text
    answer = browser.find_element(By.CSS_SELECTOR, '#answer')
    answer.send_keys(calc(int(x)))
    sumbit = browser.find_element(By.ID, 'solve')
    sumbit.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()

