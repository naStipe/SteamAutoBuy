from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import time
import pickle
from threading import Thread


def do_stuff():

    print('Doung stuff')
    while True:
        time.sleep(3)


# def open_browser():
#     driver = webdriver.Chrome()
#     driver.get('https://steamcommunity.com')
#     try:
#         load_session()
#         print('Session loaded')
#     except:
#         print('Session not found')

def save_session(driver):
    try:
        with open('session.pkl', 'wb') as session_file:
            pickle.dump(driver.get_cookies(), session_file)
            print('Session saved')

    except:
        print('Session save failed')
def load_session(driver):
    print('in load functio')
    with open('session.pkl', 'rb') as session_file:
        print('opened file')
        cookies = pickle.load(session_file)
        print('file loaded')

    for cookie in cookies:
        driver.add_cookie(  cookie)
    print('cookies added')

def start_button_click():
    do_stuff()
    messagebox.showinfo("Info", "Start button clicked")

def stop_button_click():
    messagebox.showinfo("Info", "Stop button clicked")

def exit_button_click():
    global overlay_window, driver
    save_session(driver)
    if messagebox.askyesno("Exit", "Do you want to exit?"):
        overlay_window.destroy()

    driver.close()
    exit()

def window_create():
    # Create the main window
    root = tk.Tk()
    root.title("Modern Buttons Window")

    # Create and configure themed buttons
    style = ttk.Style()
    style.configure("TButton", padding=10, font=("Helvetica", 12))

    start_button = ttk.Button(root, text="Start", command=start_button_click)
    stop_button = ttk.Button(root, text="Stop", command=stop_button_click)
    exit_button = ttk.Button(root, text="Exit", command=exit_button_click)

    # Place themed buttons in the window
    start_button.pack(pady=10)
    stop_button.pack(pady=10)
    exit_button.pack(pady=10)

    # Start the Tkinter main loop
    root.mainloop()



#----------------------------------------- MAIN BODY ------------------------------------------------#

#CONSTANTS#

chrome_options = Options()
chrome_options.add_experimental_option('detach', True)
chrome_options.add_argument('--ignore-certificate-error')
chrome_options.add_argument('--ignore-ssl-errors')
driver = webdriver.Chrome(options=chrome_options)

driver.get('https://steamcommunity.com')
load_session(driver)
driver.get('https://steamcommunity.com')

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






