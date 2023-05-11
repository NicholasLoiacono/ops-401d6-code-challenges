# Shebang line to specify the interpreter to use for running the script.
#!/usr/bin/python3

# Script: Ops 401d6 Class 13 Ops Challenge Solution
# Author: Nicholas Loiacono
# Date: 05/03/2023
# Purpose: Network Security Tool with Scapy Part 3 of 3
# Resources: Chat GPT


# Start


from scapy.all import *
import ipaddress
import sys

def scan_port(ip, port):
    # ip: The target IP address (string)
    # port: The target port (integer)

    # Create an IP packet and a TCP packet with the SYN flag set
    ip_packet = IP(dst=ip)
    tcp_packet = TCP(dport=port, flags='S')

    # Send the packet and receive a response
    response = sr1(ip_packet/tcp_packet, timeout=2, verbose=0)

    # Check the response and print appropriate message
    if response is not None:
        if response[TCP].flags == 0x12:
            # Send a RST packet to graciously close the open connection
            send_rst = sr(IP(dst=ip)/TCP(dport=port, flags='R'), verbose=0)
            print(f"Port {port}: Open")
        elif response[TCP].flags == 0x14:
            print(f"Port {port}: Closed")
    else:
        print(f"Port {port}: Filtered and silently dropped")

def is_responsive(ip):
    # ip: The target IP address (string)

    # Send ICMP echo request and wait for a response
    pkt = IP(dst=ip)/ICMP()
    reply = sr1(pkt, timeout=2, verbose=0)

    # Check the response
    if reply is None:
        print(f"{ip} is down or not responding.")
        return False
    elif reply.haslayer(ICMP):
        if int(reply[ICMP].type)==3 and int(reply[ICMP].code) in [1,2,3,9,10,13]:
            print(f"{ip} is blocking ICMP.")
            return False
        else:
            print(f"{ip} is responding.")
            return True

def main():
    # Ask the user to enter an IP address
    ip = input("Enter the IP address: ")
    
    # Perform a ping sweep on the provided IP address
    if is_responsive(ip):
        # If the host is responsive, perform a port scan
        ports = range(1, 1024)
        for port in ports:
            scan_port(ip, port)

if __name__ == "__main__":
    main()


# End