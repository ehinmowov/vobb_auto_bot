from selenium import webdriver
from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.common.action_chains import ActionChains
# from selenium.webdriver.common.keys import Keys
from time import sleep
import os
import easyocr

global options
global driver


def access_neu():
    global program_level_input, d_t
    options = Options()
    options.add_argument("user-agent= 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, "
                         "like Gecko) Chrome/60.0.3112.90 Safari/537.36' ")
    options.add_argument("interactive")
    # options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
    # options.add_argument("--headless")
    # options.add_argument("--disable-dev-shm-usage")
    # options.add_argument("--no-sandbox")

    driver = webdriver.Chrome('/Users/director/Desktop/uni-activation/chromedriver copy', options=options)
    driver.get('http://applicas.neu.edu.tr')

    un = 'mckenwin.intl@gmail.com'
    pw = 'GodwinBB30'

    username = driver.find_element_by_id('username')
    username.send_keys(un)
    # test username is mckenwin.intl@gmail.com
    sleep(1)

    password = driver.find_element_by_id('inputPassword')
    password.send_keys(pw)
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

    fn = 'Victor'
    ln = 'Ehinmowo'
    mn = 'None'
    firstname = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//*[@id='Name']")))
    firstname.send_keys(fn)
    middlename = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="MiddleName"]')))
    middlename.send_keys(mn)
    lastname = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="Surname"]')))
    lastname.send_keys(ln)

    # gender = WebDriverWait(driver, 5).until(EC.element_to_be_clickable(
    #     (By.XPATH, "//*[@id='agentApplicationForm']/div/div[1]/div[4]/div/span/span")))
    # gender.click()
    # gender_select = WebDriverWait(driver, 5).until(EC.element_to_be_clickable(
    #     (By.XPATH, "'/html/body/div[4]/div/div[3]//ul//li[text()='Female']")))
    # gender_select.click()
    gn = 'Female'
    gender = driver.find_element_by_xpath('//*[@id="agentApplicationForm"]/div/div[1]/div[4]/div/span/span/span[2]')
    gender.click()
    sleep(2)
    gender_select = WebDriverWait(driver, 50).until(EC.element_to_be_clickable((By.XPATH, f'//*[@id="Gender_listbox'
                                                                                          f'"]/li[text()="{gn}"]')))
    gender_select.click()
    sleep(1)

    birth = '11011997'
    dob = birth[:2] + '/' + birth[2:4] + '/' + birth[4:]

    date = driver.find_element_by_xpath('//*[@id="Birthdate"]')
    date.clear()
    date.send_keys(dob)
    sleep(1)

    cn = 'Nigeria'
    nationality = driver.find_element_by_xpath(
        '//*[@id="agentApplicationForm"]/div/div[2]/div[2]/div/span/span/span[1]')
    nationality.click()
    sleep(2)
    nation_select = driver.find_element_by_xpath(f'//*[@id="Nationality_listbox"]/li[text()="{cn}"]')
    nation_select.click()
    sleep(1)

    pn = 'xxxxxxxxxxx'

    passport = driver.find_element_by_xpath('//*[@id="PassportNo"]')
    passport.send_keys(pn)
    sleep(1)

    status = driver.find_element_by_xpath('//*[@id="agentApplicationForm"]/div/div[2]/div[4]/div/span/span/span[1]')
    status.click()
    sleep(2)
    status_select = driver.find_element_by_xpath('//*[@id="MaritalStatus_listbox"]/li[1]')
    status_select.click()
    sleep(1)

    fathername = driver.find_element_by_xpath('//*[@id="FatherName"]')
    fathername.send_keys(ln)
    sleep(1)

    find = driver.find_element_by_xpath('//*[@id="agentApplicationForm"]/div/div[3]/div[4]/div/span/span/span[1]')
    find.click()
    sleep(2)
    find_select = driver.find_element_by_xpath('//*[@id="HowtoFindNEU_listbox"]/li[2]')
    find_select.click()

    em = 'lollytunez@gmail.com'

    email = driver.find_element_by_xpath('//*[@id="Emergency2Email"]')
    email.send_keys('em')

    # Selecting program
    # set variable for semester
    # add faculty to form

    dg = 'International Transfer'
    sm = 'Fall'
    semester = driver.find_element_by_xpath('//*[@id="agentApplicationForm"]/div/div[8]/div[1]/div/span/span/span[1]')
    semester.click()
    sleep(2)
    semester_select = driver.find_element_by_xpath(f'//*[@id="Program1Semester_listbox"]/li[text()="{sm}"]')
    semester_select.click()
    sleep(2)

    if dg == 'International Transfer':
        program_level_input = 'Undergraduate'
    elif dg == 'International Undergraduate':
        program_level_input = 'Undergraduate'
    elif dg == 'International Master':
        program_level_input = 'Master With Thesis'
    elif dg == 'International PhD':
        program_level_input = 'PhD'
    else:
        pass

    program_level = driver.find_element_by_xpath(
        '//*[@id="agentApplicationForm"]/div/div[8]/div[2]/div/span/span/span[1]'
    ).click()

    sleep(2)
    program_level_select = driver.find_element_by_xpath(
        f'//*[@id="Program1Level_listbox"]/li[text()="{program_level_input}"]')
    program_level_select.click()
    sleep(5)

    if dg == 'International Transfer':
        direct_or_trans = driver.find_element_by_xpath(
            '//*[@id="agentApplicationForm"]/div/div[8]/div[3]/div/span/span/span[1]')
        direct_or_trans.click()
        sleep(10)

        direct_or_trans_select = WebDriverWait(driver, 50).until(
            EC.presence_of_element_located((By.XPATH, "//*[@id='Program1DirectTransfer_listbox']/li[2]")))
        print(direct_or_trans_select.is_displayed())
        direct_or_trans_select.click()
    else:
        pass

    fc = 'ARCHITECTURE '
    faculty = WebDriverWait(driver, 50).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="agentApplicationForm'
                                                                                    '"]/div/div[9]/div['
                                                                                    '1]/div/span/span/span[1]')))
    print(faculty.is_displayed())
    faculty.click()
    sleep(5)

    faculty_select = driver.find_element_by_xpath(
        f'//*[@id="Program1FacultyInstitute_listbox"]/li[starts-with(text(),"{fc}")]')
    faculty_select.click()
    sleep(2)

    sleep(2)

    pm = 'ARCHITECTURE'
    program = driver.find_element_by_xpath('//*[@id="agentApplicationForm"]/div/div[9]/div[2]/div/span/span/span[1]')
    program.click()
    sleep(5)
    try:
        program_select = driver.find_element_by_xpath(f'//*[@id="Program1Name_listbox"]/li[text()="{pm}")]')
        program_select.click()
    except:
        pm_ = pm + " "
        program_select = driver.find_element_by_xpath(f'//*[@id="Program1Name_listbox"]/li[text()="{pm_}")]')
        program_select.click()

    sleep(5)

    driver.close()


access_neu()
