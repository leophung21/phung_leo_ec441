# Network Traffic Analysis and Packet Crafting Lab

## Overview

This project explores network behavior through both packet analysis and packet construction. It combines DNS and HTTP traffic inspection with programmatic packet crafting using Scapy.

The goal is to demonstrate a full understanding of how data moves through the network stack by both observing and generating network traffic.

---

## Objectives

- Analyze DNS and HTTP traffic using packet capture data  
- Understand TCP connection establishment  
- Explore protocol layering (Ethernet → IP → TCP/UDP → Application)  
- Programmatically construct and send packets using Scapy  
- Connect theoretical networking concepts to real-world behavior  

---

## Tools Used

- Python  
- Scapy  
- Packet capture data (`.pcap`)  
- Terminal utilities (ping, curl, dig)  

---


---

## Part 1: DNS and HTTP Traffic Analysis

### DNS Observations

- DNS queries resolve domain names to IP addresses  
- DNS typically uses UDP (port 53)  
- Each query generates a corresponding response  
- TTL (Time To Live) determines caching duration  

### HTTP Observations

- HTTP operates over TCP  
- A TCP connection must be established before data transfer  
- Requests use methods such as GET  
- Responses include status codes (e.g., 200 OK)  

### Traffic Flow

The sequence observed in network communication:

---

## Part 2: Scapy Packet Crafting

Scapy allows direct interaction with the network by constructing packets manually. Unlike packet analyzers, Scapy enables both sending and receiving packets programmatically.

### Features Implemented

- Built ICMP packets manually  
- Sent ping requests using raw packets  
- Performed TCP SYN probing to check port status  
- Modified IP header fields such as TTL  

---

## Example: Building a Packet

```python
from scapy.all import IP, ICMP

packet = IP(dst="8.8.8.8") / ICMP()
packet.show()
