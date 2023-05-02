# Shebang line to specify the interpreter to use for running the script.
#!/usr/bin/python3

# Script: Ops 401d6 Class 11 Ops Challenge Solution
# Author: Nicholas Loiacono
# Date: 05/01/2023
# Purpose: Network Security Tool with Scapy Part 1 of 3
# Resources: Chat GPT


# Start

from scapy.all import *
import sys

# Define host IP and port range
host_ip = "192.168.1.248"
ports = range(1, 1024)

def scan_port(ip, port):
    # Create an IP packet and a TCP packet with the SYN flag set
    ip_packet = IP(dst=ip)
    tcp_packet = TCP(dport=port, flags='S')

    # Send the packet and receive a response
    response = sr1(ip_packet/tcp_packet, timeout=2, verbose=0)

    if response is not None:
        if response[TCP].flags == 0x12:
            # Send a RST packet to graciously close the open connection
            send_rst = sr(IP(dst=ip)/TCP(dport=port, flags='R'), verbose=0)
            print(f"Port {port}: Open")
        elif response[TCP].flags == 0x14:
            print(f"Port {port}: Closed")
    else:
        print(f"Port {port}: Filtered and silently dropped")

# Test each port in the specified range using a for loop
for port in ports:
    scan_port(host_ip, port)


# End