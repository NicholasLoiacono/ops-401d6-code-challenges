# Shebang line to specify the interpreter to use for running the script.
#!/usr/bin/python3

# Script: Ops 401d6 Class 07 Ops Challenge Solution
# Author: Nicholas Loiacono
# Date: 04/25/2023
# Purpose: File Encryption Script Part 2 of 3
# Resources: Chat GPT


# Start

# Other import statements and function definitions remain unchanged

# Define a function to encrypt a folder and all its contents recursively
def encrypt_folder(folder_path, cipher):
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            file_path = os.path.join(root, file)
            encrypt_file(file_path, cipher)
    print("Folder encrypted successfully.")

# Define a function to decrypt a folder and all its contents recursively
def decrypt_folder(folder_path, cipher):
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            file_path = os.path.join(root, file)
            decrypt_file(file_path, cipher)
    print("Folder decrypted successfully.")

# Define the main function to execute the encryption/decryption process based on user input
def main():
    # Other parts of the main function remain unchanged

    # Prompt the user to select a mode
    mode = int(input("Select a mode:\n1. Encrypt a file\n2. Decrypt a file\n3. Encrypt a message\n4. Decrypt a message\n5. Encrypt a folder\n6. Decrypt a folder\n"))

    # Check the selected mode and perform the corresponding operation
    if mode in [1, 2]:
        # Other parts of the file encryption/decryption remain unchanged
        pass
    elif mode in [3, 4]:
        # Other parts of the string encryption/decryption remain unchanged
        pass
    elif mode in [5, 6]:
        # Prompt the user to provide the folder path for encryption or decryption
        folder_path = input("Enter the folder path: ")

        # Encrypt the folder if mode 5 is selected
        if mode == 5:
            encrypt_folder(folder_path, cipher)
        # Decrypt the folder if mode 6 is selected
        elif mode == 6:
            decrypt_folder(folder_path, cipher)
    else:
        # Print an error message for invalid mode selection
        print("Invalid mode selection.")

# Execute the main function when the script is
if __name__ == '__main__':
    main()


# End