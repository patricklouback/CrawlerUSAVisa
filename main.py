import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup

from interactions import *
from xpath import xpath

from dotenv import load_dotenv
import os

load_dotenv()


email = os.environ.get('EMAIL')
password = os.environ.get('PASSWORD')


def crawler():
    url = 'https://ais.usvisa-info.com/pt-br/niv/users/sign_in'
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(url)

    # Inserindo E-mail e Senha
    write_element(driver, xpath.USER_EMAIL, email)
    time.sleep(0.2)
    write_element(driver, xpath.USER_PASSWORD, password)
    time.sleep(0.2)
    click_element(driver, xpath.POLICY_CONFIRMED)
    time.sleep(0.2)
    click_element(driver, xpath.ENTER_LOGIN)
    time.sleep(0.2)
    click_element(driver, xpath.CONTINUE)
    time.sleep(0.2)
    click_element(driver, xpath.SCHEDULE_LIST)
    time.sleep(0.2)

    html = driver.page_source
    soup = BeautifulSoup(html, "html.parser")
    element = soup.find('a', string='Reagendar entrevista')
    href = element['href']
    driver.get('https://ais.usvisa-info.com' + href)

    click_element(driver, xpath.CONTINUE_1)
    time.sleep(0.5)

    click_element(driver, xpath.DATE_APPOINTMENT)
    time.sleep(5)

    time.sleep(5)

    driver.quit()

if __name__ == '__main__':
    crawler()


