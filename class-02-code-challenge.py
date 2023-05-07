# Shebang line to specify the interpreter to use for running the script.
#!/usr/bin/python3

# Script: Ops 401d6 Class 02 Ops Challenge Solution
# Author: Nicholas Loiacono
# Date: 04/18/2023
# Purpose: Uptime Sensor Tool Part 1 of 2
# Resources: Chat GPT


# Start

#!/usr/bin/env python3
import os  # Import the os library to execute system commands
import time  # Import the time library to add delays
from datetime import datetime  # Import the datetime library to handle timestamps

# Define a function called check_ping, which takes an IP address as its argument
def check_ping(ip):
    # Send a single ICMP packet to the given IP address and store the result in the 'respond' variable
    respond = os.system("ping -c 1 " + ip)

    # Wait for 2 seconds before sending the next ICMP packet
    time.sleep(2)

    # Check the response and assign the appropriate status to the 'ping_status' variable
    if respond == 0:
        ping_status = "network is active"
    else:
        ping_status = "network is down"

    return ping_status  # Return the ping_status

# Continuously check the ping status of a given IP address
while True:
    # Get the IP address from user input
    ip_address = input("Enter an IP address: ")

    # Call the check_ping function and store the result in the 'status' variable
    status = check_ping(ip_address)

    # Get the current timestamp
    current_time = datetime.now()

    # Print the result along with the timestamp and tested IP address
    print(current_time, status, "to", ip_address)


# End