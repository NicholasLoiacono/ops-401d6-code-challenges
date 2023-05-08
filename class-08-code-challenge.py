# Shebang line to specify the interpreter to use for running the script.
#!/usr/bin/python3

# Script: Ops 401d6 Class 08 Ops Challenge Solution
# Author: Nicholas Loiacono
# Date: 04/26/2023
# Purpose: File Encryption Script Part 3 of 3
# Resources: Chat GPT


# Start

# Additional imports
import ctypes
import tkinter as tk
from tkinter import messagebox

# Other import statements and function definitions remain unchanged

# Define a function to change the desktop wallpaper
def change_wallpaper(image_path):
    SPI_SETDESKWALLPAPER = 0x0014
    ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, image_path, 3)

# Define a function to create a popup window with a ransomware message
def show_popup(message):
    root = tk.Tk()
    root.withdraw()
    messagebox.showerror("Ransomware Simulation", message)
    root.destroy()

# Define the main function to execute the encryption/decryption process based on user input
def main():
    # Other parts of the main function remain unchanged

    # Prompt the user to select a mode
    mode = int(input("Select a mode:\n1. Encrypt a file\n2. Decrypt a file\n3. Encrypt a message\n4. Decrypt a message\n5. Encrypt a folder\n6. Decrypt a folder\n7. Ransomware simulation\n"))

    # Check the selected mode and perform the corresponding operation
    if mode in [1, 2]:
        # Other parts of the file encryption/decryption remain unchanged
        pass
    elif mode in [3, 4]:
        # Other parts of the string encryption/decryption remain unchanged
        pass
    elif mode in [5, 6]:
        # Other parts of the folder encryption/decryption remain unchanged
        pass
    elif mode == 7:
        # Ransomware simulation
        wallpaper_path = input("Enter the path to the ransomware wallpaper: ")
        ransom_message = input("Enter the ransomware message for the popup: ")
        change_wallpaper(wallpaper_path)
        show_popup(ransom_message)
    else:
        # Print an error message for invalid mode selection
        print("Invalid mode selection.")

# Execute the main function when the script is
if __name__ == '__main__':
    main()


# End