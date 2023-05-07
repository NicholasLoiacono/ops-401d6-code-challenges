# Shebang line to specify the interpreter to use for running the script.
#!/usr/bin/python3

# Script: Ops 401d6 Class 03 Ops Challenge Solution
# Author: Nicholas Loiacono
# Date: 04/19/2023
# Purpose: Uptime Sensor Tool Part 2 of 2
# Resources: Chat GPT


# Start

#!/usr/bin/env python3
import os
import time
from datetime import datetime
import smtplib  # Import smtplib library for handling email
from email.message import EmailMessage  # Import EmailMessage class for creating email messages

# Function to send email
def send_email(receiver_email, subject, content):
    # Set up email message
    msg = EmailMessage()
    msg.set_content(content)
    msg['Subject'] = subject
    msg['From'] = sender_email
    msg['To'] = receiver_email

    # Log in and send the email
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
        server.login(sender_email, sender_password)
        server.send_message(msg)

# Function to check ping
def check_ping(ip):
    respond = os.system("ping -c 1 " + ip)
    time.sleep(2)
    if respond == 0:
        ping_status = "network is active"
    else:
        ping_status = "network is down"
    return ping_status

# Get sender email, password and admin email from user input
sender_email = input("Enter your email address: ")
sender_password = input("Enter your email password: ")
admin_email = input("Enter the administrator's email address: ")

# Variables to store the previous status
previous_status = None

while True:
    ip_address = input("Enter an IP address: ")
    status = check_ping(ip_address)
    current_time = datetime.now()

    # Check if the status has changed and send an email
    if previous_status is not None and status != previous_status:
        subject = f"Host Status Change for {ip_address}"
        content = f"Host {ip_address} status has changed from '{previous_status}' to '{status}' at {current_time}"
        send_email(admin_email, subject, content)

    # Print the result and update the previous_status variable
    print(current_time, status, "to", ip_address)
    previous_status = status


# End