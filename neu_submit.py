from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options
from time import sleep
import os
import easyocr

global options
global driver


def access_neu():
    options = Options()
    options.add_argument("user-agent= 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, "
                         "like Gecko) Chrome/60.0.3112.90 Safari/537.36' ")
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

    # gender = WebDriverWait(driver, 5).until(EC.element_to_be_clickable(
    #     (By.XPATH, "//*[@id='agentApplicationForm']/div/div[1]/div[4]/div/span/span")))
    # gender.click()
    # gender_select = WebDriverWait(driver, 5).until(EC.element_to_be_clickable(
    #     (By.XPATH, "'/html/body/div[4]/div/div[3]//ul//li[text()='Female']")))
    # gender_select.click()
    gn = 'Male'
    gender = driver.find_element_by_xpath('//*[@id="agentApplicationForm"]/div/div[1]/div[4]/div/span/span/span[2]')
    gender.click()
    sleep(2)
    gender_select = driver.find_element_by_xpath(f'//*[@id="Gender_listbox"]/li["{gn}"]')
    gender_select.click()
    sleep(1)

    date = driver.find_element_by_xpath('//*[@id="Birthdate"]')
    date.clear()
    date.send_keys('11011997')
    sleep(1)

    nationality = driver.find_element_by_xpath(
        '//*[@id="agentApplicationForm"]/div/div[2]/div[2]/div/span/span/span[1]')
    nationality.click()
    sleep(2)
    nation_select = driver.find_element_by_xpath('//*[@id="Nationality_listbox"]/li[3]')
    nation_select.click()
    sleep(1)

    passport = driver.find_element_by_xpath('//*[@id="PassportNo"]')
    passport.send_keys('xxxxxxxxxxx')
    sleep(1)

    status = driver.find_element_by_xpath('//*[@id="agentApplicationForm"]/div/div[2]/div[4]/div/span/span/span[1]')
    status.click()
    sleep(2)
    status_select = driver.find_element_by_xpath('//*[@id="MaritalStatus_listbox"]/li[1]')
    status_select.click()
    sleep(1)

    fathername = driver.find_element_by_xpath('//*[@id="FatherName"]')
    fathername.send_keys('Ehinmowo')
    sleep(1)

    email = driver.find_element_by_xpath('//*[@id="Emergency2Email"]')
    email.send_keys('lollytunez@gmail.com')

    # /html/body/div[4]/div/div[3]/ul/li[2]
    #
    # '//*[@id="Gender_listbox"]/li[2]'
    # gender = driver.find_element_by_xpath('//*[@id="agentApplicationForm"]/div/div[1]/div[4]/div/span/span/span[1]')
    # drop_gender = Select(gender)
    # drop_gender.select_by_visible_text('Male')
    sleep(5)

    driver.close()


access_neu()
