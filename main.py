from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from tkinter import ttk
from tkinter import messagebox
from threading import Thread
from selenium.webdriver.common.by import By
import tkinter as tk
import time
import pickle
import os


def do_looting(driver, ITEMS):
    balance = float(driver.find_element(By.CSS_SELECTOR,BALANCE_ID).text[:-1].replace(',', '.'))
    print(balance)
    driver.find_element(By.XPATH,SKIN_DATA_SWITCH).click()
    time.sleep(1)

    while balance > 1:
        print('Cycle')
        for item in ITEMS:
            get_items(driver, item['link'], item['desired_float'])


def get_items(driver, itemLink, desiredFloat):
    pageNumbers = ['0', '100', '200', '300']


    # for i in range(1):

    driver.get(itemLink+'0'+'&count=100')
    # print('Page: ' + pageNumbers[i])

    while True:
        floatValues = []
        searchButtonFound = False
        timesButtonNotFound = 0
        while not searchButtonFound:
            try:
                driver.find_element(By.CLASS_NAME, SEARCH_BUTTON_CLASS)
                searchButtonFound = True
                print('Button found')
            except:
                print('Button not found')
                timesButtonNotFound += 1
                if timesButtonNotFound >= 7:
                    print('Reloading page')
                    get_items(driver, itemLink, desiredFloat)
                    return 0

            time.sleep(1)


        items = driver.find_elements(By.CLASS_NAME, ITEM_FLOAT_CLASS)
        for item in items:
            floatText = item.find_element(By.XPATH, './/span').text
            if not floatText == '':
                itemFloat = float(floatText)
                if itemFloat < desiredFloat:
                    floatValues.append(itemFloat)
                    floatValues.append(itemFloat)
                    print(itemFloat)
                    buy_item(driver, item, itemLink, desiredFloat)

        driver.find_element(By.XPATH, '//*[@id="market_listing_filter_form"]/div/a').click()


def buy_item(driver, item, itemLink, desiredFloat):
    timeBuyFailed = 0
    try:
        item.find_element(By.XPATH, '../../../../div[2]/div[1]/div/a').click()
        time.sleep(0.3)
        print('Buy button clicked')
        checkbox = driver.find_element(By.XPATH, '//*[@id="market_buynow_dialog_accept_ssa"]')
        if not checkbox.get_attribute('checked'):
            checkbox.click()
            print('Checkbox clicked')
            time.sleep(0.1)
        else:
            print('Checkbox already cehcked')

        driver.find_element(By.XPATH, '//*[@id="market_buynow_dialog_purchase"]').click()
        time.sleep(2)
        print('By confirmed')
        driver.find_element(By.XPATH, '//*[@id="market_buynow_dialog_close"]').click()
        time.sleep(0.5)
    except:
        messagebox.showinfo("Buy failed", 'Buy failed')
        return 0

def save_session(driver):
    try:
        with open('session.pkl', 'wb') as session_file:
            pickle.dump(driver.get_cookies(), session_file)
            print('Session saved')

    except:
        print('Session save failed')
def load_session(driver):
    time.sleep(0.3)
    driver.delete_all_cookies()

    try:
        print('in load function')
        with open('session.pkl', 'rb') as session_file:
            cookies = pickle.load(session_file)
            print(cookies)

        print('Cookies loaded')
    except:
        print('cookies not found')
        return  0

    if len(cookies) == 0:
        print('Cookies are empty')
        return 0
#TODO Fix expiration date

    # if cookies[0]['expiry'] <= int(time.time()):
    #     print(int(time.time()))
    #     os.remove('session.pkl')
    #     save_session(driver)
    #     with open('session.pkl', 'rb') as session_file:
    #         print('opened file')
    #         cookies = pickle.load(session_file)
    #         print(cookies)

    try:
        for cookie in cookies:
            if cookie['domain'] == 'steamcommunity.com' or cookie['domain'] == '.steamcommunity.com':
                driver.add_cookie(cookie)

        print('cookies added')
    except:
        print('cookies not added')
        pass
# def start_button_click():
#     do_looting()
#     messagebox.showinfo("Info", "Start button clicked")
#
# def stop_button_click():
#     messagebox.showinfo("Info", "Stop button clicked")
#
# def exit_button_click():
#     global overlay_window
#     if messagebox.askyesno("Exit", "Do you want to save cookies?"):
#         save_session()
#     else:
#         os.remove('session.pkl')
#
#     driver.close()
#     exit()

def check_login(driver):
    try:
        driver.find_element(By.XPATH, LOGIN_BUTTON)
        print('Not logged in')
        return False
    except:
        print('Logged in')
        return True


def lunch(driver, ITEMS):
    driver.get(STEAM_LINK)
    load_session(driver)
    driver.get(STEAM_LINK)
    print(driver.get_cookies())
    time.sleep(1)

    if check_login(driver):
        driver.get(ITEMS[0]['link'])
        do_looting(driver, ITEMS)
    else:
        driver.delete_all_cookies()
        if messagebox.askyesno('Check log in', 'Have you logged in the account?'):
            save_session(driver)
            driver.get(ITEMS[0]['link'])
            do_looting(driver, ITEMS)

#----------------------------------------- MAIN BODY ------------------------------------------------#

#ITEMS#
ITEMS = [
#Fracture STATTREK
         # {'link': 'https://steamcommunity.com/market/listings/730/StatTrak%E2%84%A2%20MP5-SD%20%7C%20Kitbash%20%28Field-Tested%29?query=&start=', 'desired_float': 0.199},
         # {'link':'https://steamcommunity.com/market/listings/730/StatTrak%E2%84%A2%20MAG-7%20%7C%20Monster%20Call%20%28Field-Tested%29?query=&start=', 'desired_float': 0.199},
         # {'link':'https://steamcommunity.com/market/listings/730/StatTrak%E2%84%A2%20MAC-10%20%7C%20Allure%20%28Field-Tested%29?query=&start=', 'desired_float': 0.199},
         # {'link':'https://steamcommunity.com/market/listings/730/StatTrak%E2%84%A2%20Tec-9%20%7C%20Brother%20%28Field-Tested%29?query=&start=', 'desired_float': 0.199},
         # {'link': 'https://steamcommunity.com/market/listings/730/StatTrak%E2%84%A2%20Galil%20AR%20%7C%20Connexion%20%28Field-Tested%29?query=&start=', 'desired_float': 0.199},
#Fracture
         {'link': 'https://steamcommunity.com/market/listings/730/Galil%20AR%20%7C%20Connexion%20%28Field-Tested%29?query=&start=', 'desired_float': 0.199},
         {'link': 'https://steamcommunity.com/market/listings/730/MAG-7%20%7C%20Monster%20Call%20%28Field-Tested%29?query=&start=', 'desired_float': 0.199},
         {'link': 'https://steamcommunity.com/market/listings/730/MP5-SD%20%7C%20Kitbash%20%28Field-Tested%29?query=&start=', 'desired_float': 0.199},
         {'link': 'https://steamcommunity.com/market/listings/730/Tec-9%20%7C%20Brother%20%28Field-Tested%29?query=&start=', 'desired_float': 0.199},
         {'link': 'https://steamcommunity.com/market/listings/730/MAC-10%20%7C%20Allure%20%28Field-Tested%29?query=&start=', 'desired_float': 0.199}]

ITEMS_SMALL = [ITEMS[1]]
ITEMS_BIG = [ITEMS[0]]


#CONSTANTS#
STEAM_LINK = 'https://steamcommunity.com'
EXTENSION_LINK = 'https://chrome.google.com/webstore/detail/steam-inventory-helper/cmeakgjggjdlcpncigglobpjbkabhmjl'
ADD_EXTENSION_BUTTON = '/html/body/div[3]/div[2]/div/div/div[2]/div[2]/div/div/div/div'
LOGIN_BUTTON = '//*[@id="global_action_menu"]/a[2]'
BALANCE_ID = '#header_wallet_balance'
SKIN_DATA_SWITCH = '//*[@id="listings"]/div[5]/div[1]/div[1]/div[1]/div[2]/label'
ITEM_FLOAT_CLASS = 'itemfloat'
SEARCH_BUTTON_CLASS = 'open_setting_paint_seed_and_float'


chrome_options = Options()
chrome_options.add_experimental_option('detach', True)
chrome_options.add_argument('--ignore-certificate-error')
chrome_options.add_argument('--ignore-ssl-errors')
chrome_options.add_extension('1.18.41_0.crx')

driver = webdriver.Chrome(options=chrome_options)
driver.maximize_window()
lunch(driver, ITEMS_SMALL)

# driver1 = webdriver.Chrome(options=chrome_options)
# driver1.maximize_window()
# driver2 = webdriver.Chrome(options=chrome_options)
# driver2.maximize_window()
#
# thread1 = Thread(target=lunch, args=[driver1, ITEMS_BIG])
# thread1.start()
# thread2 = Thread(target=lunch, args=[driver2, ITEMS_SMALL])
# thread2.start()



# overlay_window = tk.Tk()
# overlay_window.title("Modern Buttons Window")
# style = ttk.Style()
# style.configure("TButton", padding=10, font=("Helvetica", 12))
#
# start_button = ttk.Button(overlay_window, text="Start", command=start_button_click)
# stop_button = ttk.Button(overlay_window, text="Stop", command=stop_button_click)
# exit_button = ttk.Button(overlay_window, text="Exit", command=exit_button_click)
#
# start_button.pack(pady=10)
# stop_button.pack(pady=10)
# exit_button.pack(pady=10)
#
# overlay_window.mainloop()