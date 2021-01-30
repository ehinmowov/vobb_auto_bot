from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
import os
import easyocr

global options
global driver


def access_neu():
    options = Options()
    options.add_argument("user-agent= 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_1) AppleWebKit/537.36 (KHTML, "
                         "like Gecko) Chrome/87.0.4280.141 Safari/537.36' ")
    # options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
    # options.add_argument("--headless")
    # options.add_argument("--disable-dev-shm-usage")
    # options.add_argument("--no-sandbox")

    driver = webdriver.Chrome('/Users/director/Desktop/uni-activation/chromedriver copy', options=options)
    driver.get('http://applicas.neu.edu.tr')

    username = driver.find_element_by_id('username')
    username.send_keys('mckenwin.intl@gmail.com')
    # test username is mckenwin.intl@gmail.com
    sleep(1)

    password = driver.find_element_by_id('inputPassword')
    password.send_keys('GodwinBB30')
    # test password is GodwinBB30

    sleep(1)

    login = driver.find_element_by_xpath('/html/body/div[3]/div/form/button')
    login.click()

    sleep(3)

    try:
        verification = driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/nav/div/ul/li[2]')
        verification.click()
    except:
        access_neu()

    sleep(2)


    firstname = driver.find_element_by_xpath('//*[@id="Name"]')
    firstname.send_keys('Victor')
    middlename = driver.find_element_by_xpath('//*[@id="MiddleName"]')
    middlename.send_keys('none')
    lastname = driver.find_element_by_xpath('//*[@id="Surname"]')
    lastname.send_keys('Ehinmowo')

    gender = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(
        (By.XPATH, "//*[@id='agentApplicationForm']/div/div[1]/div[4]/div/span/span")))
    gender.click()
    gender_select = WebDriverWait(driver, 50).until(EC.element_to_be_clickable(
        (By.XPATH, "//*[@id='agentApplicationForm']/div/div[1]/div[4]/div/span/span/span[1]/text('Female')")))
    gender_select.click()

    # gender = driver.find_element_by_xpath('//*[@id="agentApplicationForm"]/div/div[1]/div[4]/div/span/span/span[1]')
    # drop_gender = Select(gender)
    # drop_gender.select_by_visible_text('Male')
    sleep(20)

    driver.close()


access_neu()
