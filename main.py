from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.common.keys import Keys

import time
from datetime import datetime
import pywhatkit
from selenium.webdriver.chrome.service import Service


#
def get_inside_the_account_liat(driver):
    source = driver.find_element("link text", "כניסה / הרשמה")
    source.click()
    source = driver.find_element("id","LoginPhone")
    time.sleep(2)
    source.send_keys("0585532002")
    source = driver.find_element("id", "LoginPassword")
    # time.sleep(3)
    source.send_keys("lifr12345")
    source = driver.find_element("id", "loginButton")
    source.click()

def get_inside_the_account_ami(driver):
    source = driver.find_element("link text", "כניסה / הרשמה")
    source.click()
    source = driver.find_element("id","LoginPhone")
    time.sleep(2)
    source.send_keys("0585532002")
    source = driver.find_element("id", "LoginPassword")
    # time.sleep(3)
    source.send_keys("lifr12345")
    source = driver.find_element("id", "loginButton")
    source.click()


def open_lesson_by_time(driver):
    while True:
        ###
        currentDateAndTime = datetime.now()
        exact_time = currentDateAndTime.strftime("%H:%M")
        if exact_time == "20:34":
            register_to_spinning_lesson(driver)
            pywhatkit.sendwhatmsg("+972585532002", "קבעתי לך שיעור ספינינג", 20, 36)
            break
        if exact_time == "22:36":
            register_to_monday_buddy_pump_lesson(driver)
            pywhatkit.sendwhatmsg("+972585532002","קבעתי לך שיעור באדי פאמפ",22,37)
            break


def open_browser():
    s = Service("C:\Program Files (x86)\chromedriver.exe")
    driver = webdriver.Chrome(service=s)
    # driver.maximize_window()
    driver.get("https://www.holmesplace.co.il/place-studio/?club=210")
    get_inside_the_account_liat(driver)
    open_lesson_by_time(driver)


def register_to_spinning_lesson(driver):
    # choose_club(driver)
    time.sleep(5)
    source = driver.find_element(By.XPATH,"//*[@id='Friday']/div[2]/div/a")
    driver.execute_script("arguments[0].click();", source)
    time.sleep(5)
    source = driver.find_element(By.XPATH, "//*[@id='registerWithSeatBT']/a")
    driver.execute_script("arguments[0].click();", source)
    time.sleep(5)
    source = driver.find_element(By.XPATH, "//*[@id='lesson-reg-form']/div/div/div[1]/button/span")
    driver.execute_script("arguments[0].click();", source)
    time.sleep(5)
    source = driver.find_element("link text", "(התנתק)")
    source.click()

def register_to_monday_buddy_pump_lesson(driver):
    ####### body pump at 20:00 pm
    time.sleep(5)
    source = driver.find_element(By.XPATH, "//*[@id='pills-tab-studioContent']/div[2]/div[1]/div[1]/div[10]/div/a")
    driver.execute_script("arguments[0].click();", source)
    time.sleep(5)
    source = driver.find_element(By.XPATH, "//*[@id='registerButtonMobile']/a")
    driver.execute_script("arguments[0].click();", source)
    time.sleep(5)
    source = driver.find_element(By.XPATH, "//*[@id='lesson-reg-form']/div/div/div[1]/button/span")
    driver.execute_script("arguments[0].click();", source)
    time.sleep(5)
    source = driver.find_element("link text", "(התנתק)")
    source.click()
    time.sleep(4)
    driver.quit()



def main():
    open_browser()


main()


