from selenium import webdriver
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import time
import pickle
import threading



def open_browser():
    driver = webdriver.Chrome()
    driver.get('https://steamcommunity.com')
    try:
        load_session()
        print('Session loaded')
    except:
        print('Session not found')


def save_session():
    with open('session.pkl', 'wb') as session_file:
        pickle.dump(driver.get_cookies(), session_file)

def load_session():
    cookies = pickle.load(session_file)
    for cookie in cookies:
        driver.add_cookie(cookie)

def start_button_click():
    messagebox.showinfo("Info", "Start button clicked")

def stop_button_click():
    messagebox.showinfo("Info", "Stop button clicked")

def exit_button_click():
    save_session()
    if messagebox.askyesno("Exit", "Do you want to exit?"):
        root.destroy()

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


open_browser()

thread_window = Thread(targer=window_create)
thread_window.run()



