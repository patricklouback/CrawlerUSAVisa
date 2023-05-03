import sys
import time
from selenium import webdriver

from interactions import *
from xpath import xpath

from dotenv import load_dotenv
import os

load_dotenv()

email = os.environ.get('EMAIL')
password = os.environ.get('PASSWORD')

def crawler(attempts = 0):

    if attempts >= 2:
        print("Verifique sua conexão")
        sys.exit()

    url_base = 'https://ais.usvisa-info.com'
    url = 'https://ais.usvisa-info.com/pt-br/niv/users/sign_in'
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.set_page_load_timeout(30)

    try:
        driver.get(url)
    except:
        print('A página não carregou')
        driver.quit()
        crawler(attempts + 1)

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

    day_table = find_first_available_day(driver, xpath.TABLE_PART_2, xpath.MONTH_DIV_2, xpath.YEAR_DIV_2)

    day_table = None

    while day_table == None:
        click_element(driver, xpath.NEXT_CALENDAR)
        time.sleep(0.2)
        day_table = find_first_available_day(driver, xpath.TABLE_PART_2, xpath.MONTH_DIV_2, xpath.YEAR_DIV_2)

    time.sleep(0.2)

    driver.quit()

    save_data(day_table)

if __name__ == '__main__':
    crawler()


