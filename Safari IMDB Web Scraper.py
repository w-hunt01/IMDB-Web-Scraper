# The purpose of this file is to scrape specific data points, especially rating and overal number of views, from IMDB #
# Results are printed in an idle environment with a designated delimited character, and may be modified in another file format (such as MS Excel) and then #
#   used as an input file for another software system, such as Tableau. #

import os
import traceback
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoSuchWindowException
from selenium.common.exceptions import TimeoutException

import os
import time
import csv
from datetime import datetime

browser = webdriver.Safari()

browser.implicitly_wait(10)
time.sleep(1)

browser.get("https://www.imdb.com/?ref_=nv_homehttps://www.imdb.com/?ref_=nv_home")

time.sleep(1)

browser.maximize_window()

WebDriverWait(webdriver,60)

def LOOKUP(NAME):

    DropDownMenu = browser.find_element("xpath","//*[@id='nav-search-form']/div[1]")
    DropDownMenu.click()
    time.sleep(1)
    TitleSelect = browser.find_element("xpath","//*[@id='navbar-search-category-select-contents']/ul/li[2]/span")
    TitleSelect.click()
    time.sleep(1)

    searchbox = browser.find_element("name","q")
    searchbox.send_keys(NAME)
    searchbox.send_keys(Keys.RETURN)
    WebDriverWait(webdriver, 10)
    time.sleep(1)

    try:

        ExactMatch = browser.find_element("xpath","//*[@id='__next']/main/div[2]/div[4]/section/div/div[1]/section[2]/div[1]/div/div/a/span")
        ExactMatch.click()

        WebDriverWait(webdriver,5)    
        time.sleep(2)

        FirstResult = browser.find_element("xpath","//*[@id='__next']/main/div[2]/div[4]/section/div/div[1]/section[2]/div[2]/ul/li[1]/div[2]/div/a")
        FirstResult.click()

        time.sleep(1)

        Score = browser.find_element("xpath","//*[@id='__next']/main/div/section[1]/section/div[3]/section/section/div[2]/div[2]/div/div[1]/a/span/div/div[2]")
        print(NAME, " | ", Score.text)

    except: NoSuchElementException
    else: pass

    try:
        FirstResult = browser.find_element("xpath","//*[@id='__next']/main/div[2]/div[4]/section/div/div[1]/section[2]/div[2]/ul/li[1]/div[2]/div/a")
        FirstResult.click()

        time.sleep(1)

        Score = browser.find_element("xpath","//*[@id='__next']/main/div/section[1]/section/div[3]/section/section/div[2]/div[2]/div/div[1]/a/span/div/div[2]")
        print(NAME, " | ", Score.text)

    except: NoSuchElementException
    else: pass

    try:
        FirstResult = browser.find_element("xpath","//a[contains(@href,'" + NAME + "'")
        FirstResult.click()

        time.sleep(1)

        Score = browser.find_element("xpath","//*[@id='__next']/main/div/section[1]/section/div[3]/section/section/div[2]/div[2]/div/div[1]/a/span/div/div[2]")
        print(NAME, " | ", Score.text)

    except: NoSuchElementException
    else: pass

    time.sleep(1)

    browser.refresh()

    time.sleep(1)

# The following lines are example of potential input - file can be amended to take a .csv input file, but given current project parameters, this may not be necessary #
# For best results, use a combination of title and year of release in the IMDB search bar #
 
##LOOKUP('The Great British Baking Show: Masterclass + 2018')
##LOOKUP('Age of Glory + 2010')
##LOOKUP('Men on a Mission + 2019')

print('Blade Run One & Done')
