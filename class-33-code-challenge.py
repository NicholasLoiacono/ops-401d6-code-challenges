# Shebang line to specify the interpreter to use for running the script.
#!/usr/bin/python3

# Script: Ops 401d6 Class 33 Ops Challenge Solution
# Author: Nicholas Loiacono
# Date: 06/01/2023
# Purpose: Signature-based Malware Detection Part 3 of 3
# Resources: Chat GPT


# Start


import os
import hashlib
import time
import requests

VIRUSTOTAL_API_URL = "https://www.virustotal.com/api/v3/files/"

def get_file_info(file_path):
    with open(file_path, 'rb') as file:
        data = file.read()
        md5_hash = hashlib.md5(data).hexdigest()

    file_info = {
        "file_name": os.path.basename(file_path),
        "file_path": os.path.abspath(file_path),
        "file_size": os.path.getsize(file_path),
        "md5_hash": md5_hash,
        "timestamp": time.ctime(os.path.getmtime(file_path))
    }
    
    return file_info

def scan_directory(search_path):
    for root, dirs, files in os.walk(search_path):
        for file in files:
            file_path = os.path.join(root, file)
            file_info = get_file_info(file_path)
            print_file_info(file_info)
            virustotal_search(file_info['md5_hash'])

def print_file_info(file_info):
    print(f"\nTimestamp: {file_info['timestamp']}")
    print(f"File Name: {file_info['file_name']}")
    print(f"File Size: {file_info['file_size']} bytes")
    print(f"File Path: {file_info['file_path']}")
    print(f"MD5 Hash: {file_info['md5_hash']}")

def virustotal_search(md5_hash):
    headers = {
        "x-apikey": os.environ['API_KEY_VIRUSTOTAL']
    }
    
    response = requests.get(VIRUSTOTAL_API_URL + md5_hash, headers=headers)
    
    if response.status_code == 200:
        json_response = response.json()
        positives = json_response['data']['attributes']['last_analysis_stats']['malicious']
        print(f"VirusTotal Positives: {positives}")
    else:
        print("Error in VirusTotal API response")

def main():
    search_path = input("Enter the directory to search in: ")
    
    if not os.path.isdir(search_path):
        print("The provided path is not a valid directory.")
        return

    scan_directory(search_path)

if __name__ == "__main__":
    main()


# End