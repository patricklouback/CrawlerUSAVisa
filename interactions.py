from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


def wait_for_element_presence(driver, xpath, timeout=30):
    try:
        element_present = EC.element_to_be_clickable((By.XPATH, xpath))
        WebDriverWait(driver, timeout).until(element_present)
    except TimeoutException:
        print(f"O elemento com xpath {xpath} não foi encontrado na página após {timeout} segundos de espera.")

def click_element(driver, xpath):
    wait_for_element_presence(driver, xpath)
    driver.find_element(By.XPATH, xpath).click()

def write_element(driver, xpath, msg):
    elem = driver.find_element(By.XPATH, xpath)
    elem.clear()
    elem.send_keys(msg)
