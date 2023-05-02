# Shebang line to specify the interpreter to use for running the script.
#!/usr/bin/python3

# Script: Ops 401d6 Class 06 Ops Challenge Solution
# Author: Nicholas Loiacono
# Date: 04/24/2023
# Purpose: File Encryption Script Part 1 of 3
# Resources: Chat GPT


# Start

# Import the Fernet class from the cryptography library, and os module for file handling
from cryptography.fernet import Fernet
import os

# Define a function to generate an encryption key using Fernet
def generate_key():
    return Fernet.generate_key()

# Define a function to create a Fernet cipher object using the given encryption key
def get_cipher(key):
    return Fernet(key)

# Define a function to encrypt a file using the provided cipher object
def encrypt_file(file_path, cipher):
    # Open the file in binary read mode and read its content
    with open(file_path, 'rb') as file:
        file_data = file.read()
    # Encrypt the file data using the cipher object
    encrypted_data = cipher.encrypt(file_data)
    # Open the file in binary write mode and write the encrypted data to the file
    with open(file_path, 'wb') as file:
        file.write(encrypted_data)

# Define a function to decrypt a file using the provided cipher object
def decrypt_file(file_path, cipher):
    # Open the file in binary read mode and read the encrypted content
    with open(file_path, 'rb') as file:
        encrypted_data = file.read()
    # Decrypt the encrypted data using the cipher object
    decrypted_data = cipher.decrypt(encrypted_data)
    # Open the file in binary write mode and write the decrypted data to the file
    with open(file_path, 'wb') as file:
        file.write(decrypted_data)

# Define a function to encrypt a string using the provided cipher object
def encrypt_string(message, cipher):
    # Encrypt the message string (after encoding it) and return the encrypted string (after decoding it)
    return cipher.encrypt(message.encode()).decode()

# Define a function to decrypt a string using the provided cipher object
def decrypt_string(encrypted_message, cipher):
    # Decrypt the encrypted message string (after encoding it) and return the decrypted string (after decoding it)
    return cipher.decrypt(encrypted_message.encode()).decode()

# Define the main function to execute the encryption/decryption process based on user input
def main():
    # Generate an encryption key and create a cipher object with it
    key = generate_key()
    cipher = get_cipher(key)

    # Prompt the user to select a mode
    mode = int(input("Select a mode:\n1. Encrypt a file\n2. Decrypt a file\n3. Encrypt a message\n4. Decrypt a message\n"))

    # Check the selected mode and perform the corresponding operation
    if mode in [1, 2]:
        # Prompt the user to provide the file path for encryption or decryption
        file_path = input("Enter the filepath to the target file: ")

        # Encrypt the file if mode 1 is selected
        if mode == 1:
            encrypt_file(file_path, cipher)
            print("File encrypted successfully.")
        # Decrypt the file if mode 2 is selected
        elif mode == 2:
            decrypt_file(file_path, cipher)
            print("File decrypted successfully.")
    elif mode in [3, 4]:
        # Prompt the user to provide the cleartext string for encryption or decryption
        message = input("Enter the cleartext string: ")

        # Encrypt the string if mode 3 is selected
        if mode == 3:
            encrypted_message = encrypt_string(message, cipher)
            print("Encrypted message:", encrypted_message)
        # Decrypt the string if mode 4 is selected
        elif mode == 4:
            decrypted_message = decrypt_string(message, cipher)
            print("Decrypted message:", decrypted_message)
    else:
        # Print an error message for invalid mode selection
        print("Invalid mode selection.")

# Execute the main function when the script is
if __name__ == '__main__':
    main()

# End
