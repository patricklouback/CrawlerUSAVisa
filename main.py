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
    url_base = 'https://ais.usvisa-info.com'
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

    href = read_attribute(driver, 'href', 'a', 'Reagendar entrevista')
    driver.get(url_base + href)
    time.sleep(0.2)

    click_element(driver, xpath.CONTINUE_1)
    time.sleep(0.2)

    click_element(driver, xpath.DATE_APPOINTMENT)
    time.sleep(0.2)

    day_table = find_first_available_day(driver, xpath.TABLE_PART_1, xpath.MONTH_DIV_1, xpath.YEAR_DIV_1)
    print('Table 1',day_table)
    print(type(day_table))

    day_table = find_first_available_day(driver, xpath.TABLE_PART_2, xpath.MONTH_DIV_2, xpath.YEAR_DIV_2)
    print('Table 2',day_table)
    print(type(day_table))

    day_table = None

    while day_table == None:
        click_element(driver, xpath.NEXT_CALENDAR)
        time.sleep(0.2)
        day_table = find_first_available_day(driver, xpath.TABLE_PART_2, xpath.MONTH_DIV_2, xpath.YEAR_DIV_2)
        print('Table 2',day_table)
        print(type(day_table))



    time.sleep(5)

    driver.quit()

if __name__ == '__main__':
    crawler()


