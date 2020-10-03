from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

username = 'yourname'
password = 'yourpass'

#webd = webdriver.Chrome('./chromedriver') Windows Path
webd = webdriver.Chrome('/usr/bin/chromedriver') #Linux Path
webd.get('https://www.instagram.com/')

time.sleep(3)

element_user = webd.find_element_by_name("username")
element_user.send_keys(username)

element_pass = webd.find_element_by_name("password")
element_pass.send_keys(password,Keys.RETURN)
