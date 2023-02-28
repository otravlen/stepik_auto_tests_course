from selenium import webdriver
from selenium.webdriver.common.by import By
import time


site = "http://suninjuly.github.io/cats.html"
browser = webdriver.Chrome()
browser.get(site)
browser.find_element(By.ID, "button")

# ожидание чтобы визуально оценить результаты прохождения скрипта
time.sleep(5)
# закрываем браузер после всех манипуляций
browser.quit()



