from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options
from time import sleep
import os
import easyocr

global options
global driver


def activate_ciu(un, pw):
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

    recruitment = driver.find_element_by_id('item-4')
    recruitment.click()
    sleep(5)

    handles = driver.window_handles

    driver.switch_to_window(handles[1])



