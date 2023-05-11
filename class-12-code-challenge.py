# Shebang line to specify the interpreter to use for running the script.
#!/usr/bin/python3

# Script: Ops 401d6 Class 12 Ops Challenge Solution
# Author: Nicholas Loiacono
# Date: 05/02/2023
# Purpose: Network Security Tool with Scapy Part 2 of 3
# Resources: Chat GPT


# Start


from scapy.all import *
import ipaddress
import sys

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

def ping_sweep(network):
    # Create a list of all addresses in the given network
    net = ipaddress.ip_network(network)
    hosts = list(net.hosts())

    # Initialize count of online hosts
    online_hosts = 0

    for host in hosts:
        # Send ICMP echo request to each address and wait for a response
        pkt = IP(dst=str(host))/ICMP()
        reply = sr1(pkt, timeout=2, verbose=0)
        
        if reply is None:
            print(f"{host} is down or not responding.")
        elif reply.haslayer(ICMP):
            if int(reply[ICMP].type)==3 and int(reply[ICMP].code) in [1,2,3,9,10,13]:
                print(f"{host} is blocking ICMP.")
            else:
                print(f"{host} is responding.")
                online_hosts += 1

    print(f"Total online hosts: {online_hosts}")

def main():
    mode = input("Choose mode:\n1. TCP Port Range Scanner\n2. ICMP Ping Sweep\n")
    if mode == "1":
        host_ip = input("Enter the host IP: ")
        ports = range(1, 1024)
        for port in ports:
            scan_port(host_ip, port)
    elif mode == "2":
        network = input("Enter the network address including CIDR block: ")
        ping_sweep(network)
    else:
        print("Invalid mode selected. Exiting.")
        sys.exit()

if __name__ == "__main__":
    main()



# End