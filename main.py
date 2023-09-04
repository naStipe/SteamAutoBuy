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


def do_stuff():

    print('Doung stuff')
    while True:
        time.sleep(3)


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
        pass

    # try:
    for cookie in cookies:
        if cookie['domain'] == 'steamcommunity.com' or cookie['domain'] == '.steamcommunity.com':
            driver.add_cookie(cookie)

    print('cookies added')
# except:
#     print('cookies not added')
#     pass
def start_button_click():
    do_stuff()
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
    time.sleep(0.3)
    addExtensionButton = driver.get_element(By.XPATH, ADD_EXTENSION_BUTTON)
    addExtensionButton.click()

#----------------------------------------- MAIN BODY ------------------------------------------------#

#CONSTANTS#
EXTENSION_LINK = 'https://chrome.google.com/webstore/detail/steam-inventory-helper/cmeakgjggjdlcpncigglobpjbkabhmjl'
ADD_EXTENSION_BUTTON = '/html/body/div[3]/div[2]/div/div/div[2]/div[2]/div/div/div/div'



chrome_options = Options()
chrome_options.add_experimental_option('detach', True)
chrome_options.add_argument('--ignore-certificate-error')
chrome_options.add_argument('--ignore-ssl-errors')
driver = webdriver.Chrome(options=chrome_options)
driver.maximize_window()

driver.get('https://steamcommunity.com')
load_session(driver)
driver.get('https://steamcommunity.com')
print(driver.get_cookies())
# get_extension()

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






