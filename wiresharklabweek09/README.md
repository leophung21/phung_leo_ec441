# Wireshark Lab: DNS and HTTP Traffic Analysis

## Overview

This project demonstrates how to capture and analyze real network traffic using Wireshark, focusing on DNS resolution and HTTP communication. The goal is to connect theoretical networking concepts to real packet-level behavior.

---

## Objectives

- Capture live network traffic using Wireshark  
- Analyze DNS queries and responses  
- Inspect HTTP request and response messages  
- Understand TCP connection establishment  
- Explore protocol layering in real packets  

---

## Tools Used

- Wireshark  
- Terminal (ping, curl, dig)  
- Optional: tcpdump  

---

## Setup

### 1. Start Packet Capture

Open Wireshark and select your active network interface (Wi-Fi or Ethernet), then start capturing packets.

---

### 2. Generate Traffic

Run the following commands in a terminal:

```bash
ping -c 3 example.com
curl http://example.com
dig example.com
