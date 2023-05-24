# Shebang line to specify the interpreter to use for running the script.
#!/usr/bin/python3

# Script: Ops 401d6 Class 26 Ops Challenge Solution
# Author: Nicholas Loiacono
# Date: 05/22/2023
# Purpose: Event Logging Tool Part 1 of 3
# Resources: Chat GPT


# Start


import ctypes
import tkinter as tk
from tkinter import messagebox
import logging

# Setting up the logging configuration
logging.basicConfig(filename='app.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s')

def change_wallpaper(image_path):
    try:
        SPI_SETDESKWALLPAPER = 0x0014
        ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, image_path, 3)
        logging.info('Wallpaper changed successfully to %s', image_path)
    except Exception as e:
        logging.error('Failed to change wallpaper: %s', e)

def show_popup(message):
    try:
        root = tk.Tk()
        root.withdraw()
        messagebox.showerror("Ransomware Simulation", message)
        root.destroy()
        logging.info('Popup message displayed successfully')
    except Exception as e:
        logging.error('Failed to display popup message: %s', e)

def main():
    try:
        mode = int(input("Select a mode:\n1. Encrypt a file\n2. Decrypt a file\n3. Encrypt a message\n4. Decrypt a message\n5. Encrypt a folder\n6. Decrypt a folder\n7. Ransomware simulation\n"))
        logging.info('User selected mode %d', mode)
        if mode == 7:
            wallpaper_path = input("Enter the path to the ransomware wallpaper: ")
            ransom_message = input("Enter the ransomware message for the popup: ")
            change_wallpaper(wallpaper_path)
            show_popup(ransom_message)
        else:
            logging.warning('User selected an unsupported mode')
            print("Invalid mode selection.")
    except Exception as e:
        logging.error('Error occurred in main function: %s', e)

if __name__ == '__main__':
    main()


# End