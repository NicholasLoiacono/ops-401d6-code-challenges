# Shebang line to specify the interpreter to use for running the script.
#!/usr/bin/python3

# Script: Ops 401d6 Class 31 Ops Challenge Solution
# Author: Nicholas Loiacono
# Date: 05/30/2023
# Purpose: Signature-based Malware Detection Part 1 of 3
# Resources: Chat GPT


# Start


import os

def find_files(filename, search_path):
   result = []

   # Walking top-down from the root
   for root, dir, files in os.walk(search_path):
      if filename in files:
         result.append(os.path.join(root, filename))
   return result

def main():
   filename = input("Enter the file name to search for: ")
   search_path = input("Enter the directory to search in: ")
   
   # Ensure the search_path is a valid directory
   if not os.path.isdir(search_path):
      print("The provided path is not a valid directory.")
      return

   # Call the function to find the files
   result = find_files(filename, search_path)

   # Print results
   if len(result) > 0:
      print(f"Found {len(result)} files:")
      for res in result:
         print(res)
   else:
      print("No file found.")

if __name__ == "__main__":
   main()


# End