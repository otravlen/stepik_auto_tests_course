import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math


def logo(x):
    return str(math.log(int(x)))


class TestMainPage():
    @pytest.mark.parametrize('link', ['https://stepik.org/lesson/236895/step/1', 'https://stepik.org/lesson/236896/step/1',
                                      'https://stepik.org/lesson/236897/step/1', 'https://stepik.org/lesson/236898/step/1',
                                      'https://stepik.org/lesson/236899/step/1', 'https://stepik.org/lesson/236903/step/1',
                                      'https://stepik.org/lesson/236904/step/1', 'https://stepik.org/lesson/236905/step/1'])
    def test_entor(self, browser, link):
        browser.get(link)
        browser.implicitly_wait(5)
        btn_enter = browser.find_element(By.CSS_SELECTOR, '.navbar__auth_login')
        btn_enter.click()
        login = browser.find_element(By.CSS_SELECTOR, '#id_login_email')
        login.send_keys('karmawayso@gmail.com')
        password = browser.find_element(By.CSS_SELECTOR, '#id_login_password')
        password.send_keys('romaromazzzXXX123')
        sign = browser.find_element(By.CSS_SELECTOR, '.sign-form__btn')
        sign.click()
        time.sleep(3)
        answer = browser.find_element(By.TAG_NAME, "textarea")
        otvet = logo(time.time())
        answer.send_keys(otvet)
        button = browser.find_element(By.CLASS_NAME, "submit-submission")
        button.click()
        hint = WebDriverWait(browser, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".smart-hints__hint")))
        hint_txt = hint.text
        assert hint_txt == 'Correct!'



