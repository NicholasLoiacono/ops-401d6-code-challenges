# Shebang line to specify the interpreter to use for running the script.
#!/usr/bin/python3

# Script: Ops 401d6 Class 16 Ops Challenge Solution
# Author: Nicholas Loiacono
# Date: 05/08/2023
# Purpose: Automated Brute Force Wordlist Attack Tool Part 1 of 3
# Resources: Chat GPT


# Start

import time

def offensive_mode(word_list_file):
    with open(word_list_file, 'r') as file:
        for line in file:
            word = line.strip()  # Remove newline characters
            print(word)
            time.sleep(1)  # Delay for 1 second

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
        offensive_mode(word_list_file)
    elif mode == "2":
        target_word = input("Enter a word to search for in the word list: ")
        defensive_mode(word_list_file, target_word)
    else:
        print("Invalid mode selected. Exiting.")

if __name__ == "__main__":
    main()


# End