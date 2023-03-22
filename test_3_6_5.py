import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math


def logo(x):
    return math.log(int(x))


class TestMainPage():
    otvet = None

    @pytest.mark.parametrize('link', ['https://stepik.org/lesson/236895/step/1', 'https://stepik.org/lesson/236896/step/1',
                                      'https://stepik.org/lesson/236897/step/1', 'https://stepik.org/lesson/236898/step/1',
                                      'https://stepik.org/lesson/236899/step/1', 'https://stepik.org/lesson/236903/step/1',
                                      'https://stepik.org/lesson/236904/step/1', 'https://stepik.org/lesson/236905/step/1'] )
    def test_enter(self, browser, link):
        browser.get(link)
        browser.implicitly_wait(5)
        btn_enter = browser.find_element(By.CSS_SELECTOR, '#ember33')
        btn_enter.click()
        login = browser.find_element(By.CSS_SELECTOR, '#id_login_email')
        login.send_keys('karmawayso@gmail.com')
        password = browser.find_element(By.CSS_SELECTOR, '#id_login_password')
        password.send_keys('romaromazzzXXX123')
        sign = browser.find_element(By.CSS_SELECTOR, '.sign-form__btn')
        sign.click()
        answer = browser.find_element(By.CSS_SELECTOR, '.textarea')
        answer.send_keys(logo(time.time()))
        button = WebDriverWait(browser, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.submit-submission')))
        button.click()
        hint = WebDriverWait(browser, 5).until(EC.visibility_of_element_located()(By.CSS_SELECTOR, '.smart-hints__hint'))
        hint_text = hint.text
        assert hint_text == 'Correct!', 'тут смотреть'


        if __name__ == "__main__":
            pytest.main()