# Shebang line to specify the interpreter to use for running the script.
#!/usr/bin/python3

# Script: Ops 401d6 Class 18 Ops Challenge Solution
# Author: Nicholas Loiacono
# Date: 05/10/2023
# Purpose: Automated Brute Force Wordlist Attack Tool Part 3 of 3
# Resources: Chat GPT


# Start


import zipfile

def zip_cracker(word_list_file, zip_file):
    with open(word_list_file, 'r') as file:
        passwords = file.read().splitlines()  # Create a list of passwords
        zip = zipfile.ZipFile(zip_file)  # Load the zip file

        for password in passwords:
            try:
                zip.extractall(pwd=bytes(password, 'utf-8'))  # Try to extract the zip file with the current password
                print(f"Success! The password is {password}")
                break
            except RuntimeError:  # Raised when the password is incorrect
                print(f"Failed to extract zip file with password: {password}")
                continue

def main():
    mode = input("Choose mode:\n1. Offensive; Dictionary Iterator\n2. Defensive; Password Recognized\n3. Zip File; Brute Force\n")
    word_list_file = input("Enter the word list file path: ")

    if mode == "1":
        username = input("Enter the username: ")
        ip = input("Enter the IP address: ")
        offensive_mode(word_list_file, username, ip)
    elif mode == "2":
        target_word = input("Enter a word to search for in the word list: ")
        defensive_mode(word_list_file, target_word)
    elif mode == "3":
        zip_file = input("Enter the zip file path: ")
        zip_cracker(word_list_file, zip_file)
    else:
        print("Invalid mode selected. Exiting.")

if __name__ == "__main__":
    main()


# End