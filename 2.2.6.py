from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

site = "http://suninjuly.github.io/execute_script.html"
browser = webdriver.Chrome()
browser.get(site)
try:
    x = browser.find_element(By.CSS_SELECTOR, '#input_value').text
    answer = browser.find_element(By.CSS_SELECTOR, '#answer')
    answer.send_keys(calc(int(x)))

    check = browser.find_element(By.CSS_SELECTOR, '#robotCheckbox')
    check.click()
    sumbit = browser.find_element(By.CSS_SELECTOR, '.btn-primaryx`')
    browser.execute_script("return arguments[0].scrollIntoView(true);", sumbit)
    radio = browser.find_element(By.CSS_SELECTOR, '#robotsRule')
    radio.click()
    sumbit.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()



