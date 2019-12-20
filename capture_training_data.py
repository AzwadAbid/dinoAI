from selenium import webdriver
import selenium.webdriver.common.keys as Keys
import time
import threading
from capture import capture_feed 

driver = webdriver.Chrome("./chromedriver.exe")
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])

driver.get(('chrome://dino/'))
time.sleep(2)
page = driver.find_element_by_class_name('offline')
page.send_keys(u'\ue00d')

capture_feed.start()

try:
    while True:
        pass
except KeyboardInterrupt:
    pass
