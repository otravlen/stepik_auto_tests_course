from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time


try:
    site = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(site)
    num1 = browser.find_element(By.CSS_SELECTOR, '#num1')
    num2 = browser.find_element(By.CSS_SELECTOR, '#num2')
    summ = str(int(num1.text) + int(num2.text))
    print(summ)
    select = Select(browser.find_element(By.CSS_SELECTOR, "#dropdown"))
    select.select_by_value(summ)
    sumbit = browser.find_element(By.CSS_SELECTOR, '.btn-default')
    sumbit.click()



finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()