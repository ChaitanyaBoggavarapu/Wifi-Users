# -*- coding: utf-8 -*-
"""
Created on Thu Sep  5 03:02:54 2019

@author: Abhilash
"""

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import schedule
import datetime
 

#print (str(currentDT))
people= list()

def job():
    numberofusers = 0
    currentDT = datetime.datetime.now()
    driver = webdriver.Chrome()
    #driver.get("http://www.python.org")
    driver.get("https://admin:Password@routerlogin.net/")
    
    #a = driver.find_element_by_id("AttachedDevices-condition")
    
    driver.switch_to.frame("page")
    
    b = driver.page_source
    
    result = b.find('<span id="AttachedDevices-condition" class="Condition-normal">')
    #print(b[result+62])
    if (b[result+63]!='<'):
        #result1 = b[result+63]
        numberofusers = str(b[result+62])+str(b[result+63])
        print('in if')
    else:
        numberofusers = str(b[result+62])
        print('in else')
    #print(numberofusers)
    driver.implicitly_wait(15)
    
    driver.quit()
    people.append(str(currentDT)+'number of users' + (numberofusers))
    return people
schedule.every(2).minutes.do(job)

while True:
    schedule.run_pending()
    time.sleep(1)


