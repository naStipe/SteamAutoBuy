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


def do_looting():
    # balance = float(driver.find_element(By.CSS_SELECTOR,BALANCE_ID).text[-5])
    # print(balance)
    driver.find_element(By.XPATH,SKIN_DATA_SWITCH).click()
    time.sleep(1)

    # time.sleep(5)
    #
    get_items('https://steamcommunity.com/market/listings/730/Dual%20Berettas%20%7C%20Stained%20%28Field-Tested%29?query=&start=0&count=100', 0.199)
    # print(items.find_element(By.XPATH, ITEM_FLOAT).text)

def get_items(itemLink, desired_float):
    global floatValues
    driver.get(itemLink)
    time.sleep(1)
    foundFound = False
    while not foundFound:
        try:
            driver.find_element(By.CLASS_NAME, SEARCH_BUTTON_CLASS)
            foundFound = True
            print('Button found')
        except:
            print('Button not found')

        time.sleep(5)


    items = driver.find_elements(By.CLASS_NAME, ITEM_FLOAT_CLASS)
    for item in items:
        itemFloat = float(item.find_element(By.XPATH, './/span').text)
        if itemFloat < desired_float:
            floatValues.append(itemFloat)
            print(itemFloat)
            buy_item(item)

def buy_item(item):
    item.find_element(By.XPATH, '../../../../div[2]/div[1]/div/a').click()
    time.sleep(100)

def save_session():
    try:
        with open('session.pkl', 'wb') as session_file:
            pickle.dump(driver.get_cookies(), session_file)
            print('Session saved')

    except:
        print('Session save failed')
def load_session():
    time.sleep(0.3)
    driver.delete_all_cookies()

    try:
        print('in load functio')
        with open('session.pkl', 'rb') as session_file:
            print('opened file')
            cookies = pickle.load(session_file)
            print(cookies)

            if cookies[0]['expiry'] <= int(time.sleep()):
                os.remove('session.pkl')
                save_session()

    except:
        print('cookies not found')
        return  0

    try:
        for cookie in cookies:
            if cookie['domain'] == 'steamcommunity.com' or cookie['domain'] == '.steamcommunity.com':
                driver.add_cookie(cookie)

        print('cookies added')
    except:
        print('cookies not added')
        pass
def start_button_click():
    do_looting()
    messagebox.showinfo("Info", "Start button clicked")

def stop_button_click():
    messagebox.showinfo("Info", "Stop button clicked")

def exit_button_click():
    global overlay_window
    if messagebox.askyesno("Exit", "Do you want to save cookies?"):
        save_session()
    else:
        os.remove('session.pkl')

    driver.close()
    exit()


def check_login():
    try:
        driver.find_element(By.XPATH, LOGIN_BUTTON)
        print('Not logged in')
        return False
    except:
        print('Logged in')
        return True


#----------------------------------------- MAIN BODY ------------------------------------------------#

#CONSTANTS#
STEAM_LINK = 'https://steamcommunity.com'
EXTENSION_LINK = 'https://chrome.google.com/webstore/detail/steam-inventory-helper/cmeakgjggjdlcpncigglobpjbkabhmjl'
ADD_EXTENSION_BUTTON = '/html/body/div[3]/div[2]/div/div/div[2]/div[2]/div/div/div/div'
MP5_LINK = {'link':'https://steamcommunity.com/market/listings/730/StatTrak%E2%84%A2%20MP5-SD%20%7C%20Kitbash%20%28Field-Tested%29?query=&start=0&count=100', 'desired_float': 0.199}
MAG7_LINK = {'link':'https://steamcommunity.com/market/listings/730/StatTrak%E2%84%A2%20MAG-7%20%7C%20Monster%20Call%20%28Field-Tested%29?query=&start=0&count=100', 'desired_float': 0.199}
MAC10_LINK = {'link':'https://steamcommunity.com/market/listings/730/StatTrak%E2%84%A2%20MAC-10%20%7C%20Allure%20%28Field-Tested%29?query=&start=0&count=100', 'desired_float': 0.199}
TEC9_LINK = {'link':'https://steamcommunity.com/market/listings/730/StatTrak%E2%84%A2%20Tec-9%20%7C%20Brother%20%28Field-Tested%29?query=&start=0&count=100', 'desired_float': 0.199}
GALIL_LINK = {'link':'https://steamcommunity.com/market/listings/730/StatTrak%E2%84%A2%20Galil%20AR%20%7C%20Connexion%20%28Field-Tested%29?query=&start=0&count=100', 'desired_float': 0.199}
LOGIN_BUTTON = '//*[@id="global_action_menu"]/a[2]'
BALANCE_ID = '#header_wallet_balance'
SKIN_DATA_SWITCH = '//*[@id="listings"]/div[5]/div[1]/div[1]/div[1]/div[2]/label'
ITEM_FLOAT_CLASS = 'itemfloat'
SEARCH_BUTTON_CLASS = 'open_setting_paint_seed_and_float'
floatValues = []


chrome_options = Options()
chrome_options.add_experimental_option('detach', True)
chrome_options.add_argument('--ignore-certificate-error')
chrome_options.add_argument('--ignore-ssl-errors')
chrome_options.add_extension('1.18.41_0.crx')
driver = webdriver.Chrome(options=chrome_options)
driver.maximize_window()

driver.get(STEAM_LINK)
load_session()
driver.get(STEAM_LINK)
print(driver.get_cookies())
time.sleep(1)

if check_login():
    driver.get(MP5_LINK['link'])
    do_looting()
else:
    os.remove('session.pkl')
    if messagebox.askyesno('Check log in', 'Have you logged in the account?'):
        save_session()
        driver.get(MP5_LINK['link'])
        do_looting()

driver.get(MP5_LINK['link'])
do_looting()

overlay_window = tk.Tk()
overlay_window.title("Modern Buttons Window")
style = ttk.Style()
style.configure("TButton", padding=10, font=("Helvetica", 12))

start_button = ttk.Button(overlay_window, text="Start", command=start_button_click)
stop_button = ttk.Button(overlay_window, text="Stop", command=stop_button_click)
exit_button = ttk.Button(overlay_window, text="Exit", command=exit_button_click)

start_button.pack(pady=10)
stop_button.pack(pady=10)
exit_button.pack(pady=10)

overlay_window.mainloop()

