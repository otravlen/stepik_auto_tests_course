from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

current_dir = os.path.abspath(os.path.dirname(__file__))
file_path = os.path.join(current_dir, 'file.txt')


site = "http://suninjuly.github.io/file_input.html"
browser = webdriver.Chrome()
browser.get(site)

try:
    file = open('file.txt', 'a')
    fname = browser.find_element(By.CSS_SELECTOR, "[name='firstname']")
    fname.send_keys('Наталья')
    lname = browser.find_element(By.CSS_SELECTOR, "[name='lastname']")
    lname.send_keys('Морская')
    email = browser.find_element(By.CSS_SELECTOR, "[name='email']")
    email.send_keys(By.CSS_SELECTOR, 'Пехота')
    sendfile = browser.find_element(By.CSS_SELECTOR, '#file')
    sendfile.send_keys(file_path)
    sumbit = browser.find_element(By.CSS_SELECTOR, '.btn-primary')
    sumbit.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()