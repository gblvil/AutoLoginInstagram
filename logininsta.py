import hashlib
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

username = 'yourname'
password = 'yourpass'


webd = webdriver.Chrome('C:/Selenium/chromedriver.exe')  # Windows Path
# webd = webdriver.Chrome('/usr/bin/chromedriver')  # Linux Path
webd.get('https://www.instagram.com/')

time.sleep(3)
element_button = webd.find_element_by_xpath(
    "/html/body/div[4]/div/div/button[1]")
element_button.click()

time.sleep(3)
element_user = webd.find_element_by_name("username")
element_user.send_keys(username)

element_pass = webd.find_element_by_name("password")
element_pass.send_keys(password, Keys.RETURN)

time.sleep(3)
element_Login = webd.find_element_by_xpath(
    "/html/body/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div[1]/div[3]/button/div")
element_Login.click()
