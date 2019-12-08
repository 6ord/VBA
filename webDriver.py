from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import time

EXE_PATH = 'C:\\Users\\u1157415\\AppData\\Local\\Google\\Chrome\\Application\\chromedriver.exe'
#EXE_PATH = 'C:\\Program Files (x86)\\Mozilla Firefox\\firefox.exe'
browser = webdriver.Chrome(executable_path=EXE_PATH)
#driver = webdriver.Firefox(executable_path=EXE_PATH)
browser.get('http://inventwithpython.com')
time.sleep(3)
cwm = browser.find_element_by_link_text('Coding with Minecraft')
#type(cwm)
cwm.click()

time.sleep(3)

browser.get('https://www.insurancehotline.com/')
pc = browser.find_element_by_id('postalCode')
pc.send_keys('M4C 1A1')
#submit = browser.find_element_by_link_text('Get Quotes Now')
#submit.click()

browser.find_element_by_class_name('button-accent').click()

#browser.find_element_by_tag_name('html').send_keys(Keys.TAB)
#pc = browser.find_element_by_id('postalCode')
#browser.find_element_by_tag_name('html').send_keys('M4C 1A1')
#browser.find_element_by_link_text('Continue').click()
#browser.find_element_by_tag_name('html').send_keys(Keys.ENTER)
