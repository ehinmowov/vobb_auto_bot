from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options
from time import sleep
import os
import easyocr

global options
global driver

options = Options()
# options.add_argument("user-agent= 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_1) AppleWebKit/537.36 (KHTML, "
#                      "like Gecko) Chrome/87.0.4280.141 Safari/537.36' ")
# # options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
# # options.add_argument("--headless")
# # options.add_argument("--disable-dev-shm-usage")
# # options.add_argument("--no-sandbox")
#
driver = webdriver.Chrome('/Users/director/Desktop/uni-activation/chromedriver copy', options=options)


def access_ciu(un, pw, fn, ln, gn, dob, pn, em, pob, ct, cn, dg, pm):
    global program_level_input
    options = Options()
    options.add_argument("user-agent= 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_1) AppleWebKit/537.36 (KHTML, "
                         "like Gecko) Chrome/87.0.4280.141 Safari/537.36' ")
    # options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
    # options.add_argument("--headless")
    # options.add_argument("--disable-dev-shm-usage")
    # options.add_argument("--no-sandbox")

    driver = webdriver.Chrome('/Users/director/Desktop/uni-activation/chromedriver copy', options=options)
    driver.get('http://srs.ciu.edu.tr')
    username = driver.find_element_by_id('email')
    username.send_keys(un)
    # test username is 1527
    password = driver.find_element_by_id('password')
    password.send_keys(pw)
    # test password is gKc68Wj6

    cap = driver.find_element_by_id('captcha')
    base_cap = cap.screenshot_as_png
    sleep(5)

    reader = easyocr.Reader(['en'])
    result = reader.readtext(base_cap)
    # getting both the text and the confidence (if confidence is less than 0.85, the bot need to refresh the captcha
    # and take a new screenshot
    recap_input = result[0][1]
    confidence = result[0][2]
    # print(recap_input)
    # print(confidence)
    while confidence < 0.7:
        refresh = driver.find_element_by_xpath('/html/body/div/div/div/div/div[2]/div[2]/div/div/div/form/div['
                                               '3]/div/span')
        refresh.click()
        sleep(2)

        cap = driver.find_element_by_id('captcha')
        base_cap = cap.screenshot_as_png

        reader = easyocr.Reader(['en'])
        result = reader.readtext(base_cap)
        recap_input = result[0][1]
        confidence = result[0][2]
        # print(recap_input)
        # print(confidence)

        if confidence < 0.69:
            continue
        else:
            print("Successful")
            break

    captcha = driver.find_element_by_xpath('/html/body/div/div/div/div/div[2]/div[2]/div/div/div/form/div[3]/div/div['
                                           '2]/input')
    captcha.send_keys(recap_input)

    login = driver.find_element_by_id('submit-btn')
    login.click()
    sleep(5)

    try:
        recruitment = driver.find_element_by_id('item-4')
        recruitment.click()
        sleep(5)
    except:
        driver.quit()
        sleep(1)
        access_ciu()

    main_page = driver.current_window_handle
    for handle in driver.window_handles:
        if handle != main_page:
            print(handle)
            next_page = handle
            break

    driver.switch_to.window(next_page)

    # first_window = driver.current_window_handle()

    # windows = driver.window_handles()
    # next_window = windows[1]
    # driver.switch_to_window(next_window)
    sleep(5)

    new_application = driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/ul/li[3]/a/i')
    new_application.click()
    sleep(5)

    # def step_1(fn, ln, gn, dob, pn, em, pob, ct, cn):

    firstname = driver.find_element_by_xpath('//*[@id="m_wizard_form_step_1"]/div/div/div[1]/div[3]/div[1]/div/input')
    firstname.send_keys(fn)
    middlename = driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div/div[2]/div[3]/form/div[1]/div['
                                              '1]/div/div/div[1]/div[3]/div[2]/div/input')
    middlename.send_keys('none')
    lastname = driver.find_element_by_xpath('//*[@id="m_wizard_form_step_1"]/div/div/div[1]/div[3]/div[3]/div/input')
    lastname.send_keys(ln)
    gender = driver.find_element_by_id('genderSelect')
    drop_gender = Select(gender)
    drop_gender.select_by_visible_text(gn)
    date = driver.find_element_by_id('dob')
    date.send_keys(dob)
    # send the date of birth in this format mmddyyyy (example: 03131998
    telephone = driver.find_element_by_xpath('//*[@id="m_wizard_form_step_1"]/div/div/div[1]/div[5]/div[2]/div/select')
    drop_telephone = Select(telephone)
    drop_telephone.select_by_visible_text('TURKISH REPUBLIC OF NORTHERN CYPRUS (90)')
    phone = driver.find_element_by_id('phone')
    phone.send_keys('5488241161')
    passport = driver.find_element_by_xpath('//*[@id="m_wizard_form_step_1"]/div/div/div[1]/div[6]/div[2]/div/input')
    passport.send_keys(pn)
    email = driver.find_element_by_xpath('//*[@id="m_wizard_form_step_1"]/div/div/div[1]/div[5]/div[1]/div/input')
    email.send_keys(em)
    id = driver.find_element_by_xpath('//*[@id="m_wizard_form_step_1"]/div/div/div[1]/div[6]/div[1]/div/input')
    id.send_keys('vobb.io')
    place_of_birth = driver.find_element_by_xpath('//*[@id="m_wizard_form_step_1"]/div/div/div[1]/div[7]/div/div/input')
    place_of_birth.send_keys(pob)
    fathers_name = driver.find_element_by_xpath('//*[@id="m_wizard_form_step_1"]/div/div/div[3]/div/div[1]/div/input')
    fathers_name.send_keys(ln)
    mothers_name = driver.find_element_by_xpath('//*[@id="m_wizard_form_step_1"]/div/div/div[3]/div/div[2]/div/input')
    mothers_name.send_keys(fn)
    address = driver.find_element_by_xpath('//*[@id="m_wizard_form_step_1"]/div/div/div[5]/div[2]/div[1]/input')
    address.send_keys(f'{ln} apt')
    city = driver.find_element_by_xpath('//*[@id="m_wizard_form_step_1"]/div/div/div[5]/div[2]/div[2]/div/input')
    city.send_keys(ct)
    country = driver.find_element_by_id('countrySelect')
    drop_country = Select(country)
    drop_country.select_by_visible_text(cn)
    # country should come in all caps
    citizenship = driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div/div[2]/div[3]/form/div[1]/div['
                                               '1]/div/div/div[5]/div[4]/div[2]/select')
    drop_citizenship = Select(citizenship)
    drop_citizenship.select_by_visible_text(cn)
    cont = driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div/div[2]/div[3]/form/div[2]/div/div/div['
                                        '3]/a[2]')
    cont.click()
    sleep(2)

    # def step_2(dg, pm):
    semester = driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div/div[2]/div[3]/form/div[1]/div['
                                            '2]/div/div/div/div[2]/div[1]/div/select')
    drop_semester = Select(semester)
    drop_semester.select_by_index(1)
    degree = driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div/div[2]/div[3]/form/div[1]/div['
                                          '2]/div/div/div/div[2]/div[2]/div/select')
    drop_degree = Select(degree)
    drop_degree.select_by_visible_text(dg)

    if dg == 'International Transfer':
        program_level_input = 1
    elif dg == 'International Undergraduate':
        program_level_input = 2
    elif dg == 'International Master':
        program_level_input = 1
    elif dg == 'International PhD':
        program_level_input = 0
    else:
        pass

    sleep(2)
    program_level = driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div/div[2]/div[3]/form/div[1]/div['
                                                 '2]/div/div/div/div[4]/div[1]/div/select')
    drop_program_level = Select(program_level)
    drop_program_level.select_by_index(program_level_input)
    sleep(2)
    program = driver.find_element_by_name('program')
    drop_program = Select(program)
    drop_program.select_by_visible_text(pm)

    cont = driver.find_element_by_xpath('//*[@id="m_form"]/div[2]/div/div/div[3]/a[2]')
    cont.click()
    sleep(1)
    next = driver.find_element_by_xpath('//*[@id="m_form"]/div[2]/div/div/div[3]/a[2]')
    next.click()
    sleep(1)
    checkbox = driver.find_element_by_xpath('//*[@id="m_wizard_form_step_5"]/div/div/div[4]/div/div/label')
    checkbox.click()

    finish = driver.find_element_by_xpath('//*[@id="m_form"]/div[2]/div/div/div[3]/a[1]')
    finish.click()


    sleep(10)



