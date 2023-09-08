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
    balance = float(driver.find_element(By.CSS_SELECTOR,BALANCE_ID).text[-5])
    print(balance)
    driver.find_element(By.XPATH,SKIN_DATA_SWITCH).click()

    items = driver.find_elements(By.CLASS_NAME, ITEM_ROW)
    print(items)

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
        print('in load functio')
        with open('session.pkl', 'rb') as session_file:
            print('opened file')
            cookies = pickle.load(session_file)
            print(cookies)
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
    global overlay_window, driver
    if messagebox.askyesno("Exit", "Do you want to save cookies?"):
        save_session(driver)
    else:
        os.remove('session.pkl')

    driver.close()
    exit()


def get_extension():
    global driver
    driver.get(EXTENSION_LINK)
    if messagebox.askyesno('Extension installation', 'Has the extension been installed?'):
        driver.get(MP5_LINK)

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
MP5_LINK = 'https://steamcommunity.com/market/listings/730/MP5-SD%20%7C%20Kitbash%20%28Field-Tested%29#'
LOGIN_BUTTON = '//*[@id="global_action_menu"]/a[2]'
BALANCE_ID = '#header_wallet_balance'
SKIN_DATA_SWITCH = '//*[@id="listings"]/div[5]/div[1]/div[1]/div[1]/div[2]/label'
ITEM_ROW = '.market_listing_row .market_recent_listing_row .listing_4312814024297907184'



chrome_options = Options()
chrome_options.add_experimental_option('detach', True)
chrome_options.add_argument('--ignore-certificate-error')
chrome_options.add_argument('--ignore-ssl-errors')
driver = webdriver.Chrome(options=chrome_options)
driver.maximize_window()

driver.get(STEAM_LINK)
load_session(driver)
driver.get(STEAM_LINK)
print(driver.get_cookies())

if check_login():
    get_extension()
else:
    if messagebox.askyesno('Check log in', 'Have you logged in the account?'):
        get_extension()


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






