import os
import platform
import random
import string
import time
from random import choice
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
import tkinter as tk
from base.base import Base as base

linux_wd = "/meet_tests/"
windows_wd = "\meet_tests\\"


@pytest.mark.usefixtures('get_call_join_page')
class TestCallPageCreate:

    def test_get_page(self, get_url):
        self.driver.get(get_url)

    def test_switch_offmic(self):
        element = base(self.driver).is_visible_xpath(
            '//*[@id="app"]/div/div[3]/div/div[2]/div/div[2]/div/div[2]/div[1]/div/div[2]/label/div'
        )
        time.sleep(3)
        self.driver.execute_script("arguments[0].click();", element)
        assert base(self.driver).is_visible_xpath(
            '//*[@id="app"]/div/div[3]/div/div[2]/div/div[2]/div/div[2]/div[1]/div/div[2]/div/div/div'
        ).text == 'Выкл'

    def test_switch_offcam(self):
        element = base(self.driver).is_visible_xpath(
            '//*[@id="app"]/div/div[3]/div/div[2]/div/div[2]/div/div[2]/div[1]/div/div[1]/label/div'
        )
        time.sleep(2)
        self.driver.execute_script("arguments[0].click();", element)
        assert base(self.driver).is_visible_xpath(
            '//*[@id="app"]/div/div[3]/div/div[2]/div/div[2]/div/div[2]/div[1]/div/div[1]/div/div/div'
        ).text == 'Выкл'

    def test_join_yesname(self, worker_id):
        base(self.driver).is_visible_class('join-button').click()
        time.sleep(3)
        base(self.driver).is_visible_tag('input').send_keys(
            f'bot_0_{self.driver.capabilities["browserName"]}_{self.driver.capabilities["browserVersion"]}'
        )
        base(self.driver).is_visible_class('join-button').click()
        assert base(self.driver).is_visible_class('without-video')  # Переход на экран звонка

    def test_get_url(self, get_url):
        WebDriverWait(self.driver, timeout=30).until(
            ec.element_to_be_clickable((By.CLASS_NAME, 'invite-buttons-wrapper'
                                        )))
        self.driver.find_element_by_class_name("toggle-wrapper").click()
        self.driver.find_element_by_xpath(
            "//*[@id='app']/div/div[3]/div/div/div/div[3]/div[1]/div/div[2]/div/div/div/div/div/div[2]/button[4]"
        ).click()
        root = tk.Tk()
        root.withdraw()
        referal = root.clipboard_get()
        with open("Constants.py", "r") as file:
            lines = file.readlines()
            lines[-1] = f"REF_URL = '{referal}'"
            new = "".join(lines)
        with open("Constants.py", "w") as file:
            file.write(new)

    def test_chat_buttton(self):
        base(self.driver).is_visible_class('icon-chat').click()
        time.sleep(1)
        assert base(self.driver).is_visible_class('shift-stage')  # Появилось окно чата

    def test_send_messages_to_chat(self, get_data):
        mes = get_data
        if mes[1] == mes[2]:
            m_count = mes[1]
        base(self.driver).is_visible_css("#roomTextarea").click()
        base(self.driver).is_visible_css(".shift-stage > div").click()
        for i in range(mes[0]):
            if mes[1] == mes[2]:
                message = "".join(choice(string.ascii_lowercase) for i in range(m_count))
            else:
                message = "".join(choice(string.ascii_lowercase) for i in range(random.randrange(mes[1], mes[2])))
            self.driver.find_element_by_css_selector("#roomTextarea").send_keys(message)
            self.driver.find_element_by_css_selector(
                "#room-footer > div > div.vac-icon-textarea > div.vac-svg-button > svg").click()


@pytest.mark.usefixtures('get_call_join_page')
class TestSecond:

    def test_get_page(self, get_ref):
        while get_ref == None:
            continue
        self.driver.get(get_ref)

    def test_switch_offmic(self):
        element = base(self.driver).is_visible_xpath(
            '//*[@id="app"]/div/div[3]/div/div[2]/div/div[2]/div/div[2]/div[1]/div/div[2]/label/div'
        )
        time.sleep(3)
        self.driver.execute_script("arguments[0].click();", element)
        assert base(self.driver).is_visible_xpath(
            '//*[@id="app"]/div/div[3]/div/div[2]/div/div[2]/div/div[2]/div[1]/div/div[2]/div/div/div'
        ).text == 'Выкл'

    def test_switch_offcam(self):
        element = base(self.driver).is_visible_xpath(
            '//*[@id="app"]/div/div[3]/div/div[2]/div/div[2]/div/div[2]/div[1]/div/div[1]/label/div'
        )
        time.sleep(2)
        self.driver.execute_script("arguments[0].click();", element)
        assert base(self.driver).is_visible_xpath(
            '//*[@id="app"]/div/div[3]/div/div[2]/div/div[2]/div/div[2]/div[1]/div/div[1]/div/div/div'
        ).text == 'Выкл'

    def test_join_yesname(self, worker_id):
        base(self.driver).is_visible_class('join-button').click()
        time.sleep(3)
        id = worker_id[-1]
        worker = int(id)+1
        base(self.driver).is_visible_tag('input').send_keys(
            f'bot_{worker}_{self.driver.capabilities["browserName"]}_{self.driver.capabilities["browserVersion"]}'
        )
        base(self.driver).is_visible_class('join-button').click()
        assert base(self.driver).is_visible_class('without-video')  # Переход на экран звонка

    def test_chat_buttton(self):
        base(self.driver).is_visible_class('icon-chat').click()
        time.sleep(1)
        assert base(self.driver).is_visible_class('shift-stage')  # Появилось окно чата

    def test_send_messages_to_chat(self, get_data, worker_id):
        mes = get_data
        if mes[1] == mes[2]:
            m_count = mes[1]
        base(self.driver).is_visible_css("#roomTextarea").click()
        base(self.driver).is_visible_css(".shift-stage > div").click()
        for i in range(mes[0]):
            if mes[1] == mes[2]:
                message = "".join(choice(string.ascii_lowercase) for i in range(m_count))
            else:
                message = "".join(choice(string.ascii_lowercase) for i in range(random.randrange(mes[1], mes[2])))
            self.driver.find_element_by_css_selector("#roomTextarea").send_keys(message)
            self.driver.find_element_by_css_selector(
                "#room-footer > div > div.vac-icon-textarea > div.vac-svg-button > svg").click()




