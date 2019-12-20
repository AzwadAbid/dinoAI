from selenium import webdriver
import selenium.webdriver.common.keys as Keys
import time
import threading
from capture import capture_feed
import os, shutil

folder = './images/'
for filename in os.listdir(folder):
    file_path = os.path.join(folder, filename)
    try:
        if os.path.isfile(file_path) or os.path.islink(file_path):
            os.unlink(file_path)
        elif os.path.isdir(file_path):
            shutil.rmtree(file_path)
    except Exception as e:
        print('Failed to delete %s. Reason: %s' % (file_path, e))
 
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
