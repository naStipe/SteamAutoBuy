from selenium import webdriver
import time

def open_browser():
    driver = webdriver.Chrome()
    driver.get('https://steamcommunity.com')
    time.sleep(30)


#----------------------------------------- MAIN BODY ------------------------------------------------#

#CONSTANTS#



open_browser()

