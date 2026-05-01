# TCP Reliability Simulator

A Python simulation that demonstrates how TCP achieves reliable data transfer over an unreliable network.

This project implements and compares three foundational transport-layer protocols:

- Stop-and-Wait  
- Go-Back-N (GBN)  
- Selective Repeat (SR)  

---

## Overview

At the network layer, protocols like IP provide best-effort delivery, meaning:

- Packets can be lost  
- Packets may arrive out of order  
- No delivery guarantees exist  

The transport layer solves this problem by introducing reliability mechanisms such as:

- Acknowledgments (ACKs)  
- Sequence numbers  
- Retransmissions  
- Sliding windows  

This simulator models these behaviors to show how reliable communication is built on top of an unreliable channel.

---

## Concepts Demonstrated

### Stop-and-Wait

- Sends one packet at a time  
- Waits for acknowledgment before continuing  
- Retransmits on timeout  

Simple and correct, but highly inefficient in high-latency networks  

---

### Go-Back-N (GBN)

- Sends multiple packets within a window  
- Uses cumulative acknowledgments  
- If a packet is lost, retransmits that packet and all following packets  

Improves throughput but can waste bandwidth  

---

### Selective Repeat (SR)

- Sends multiple packets within a window  
- Buffers out-of-order packets at the receiver  
- Only retransmits the specific lost packets  

Most efficient approach, but more complex to implement  

---

## How the Simulation Works

- The network is simulated using a random packet loss model  
- Each protocol is implemented as a separate function  
- The sender and receiver behaviors are printed step-by-step  
- Packet loss triggers retransmission logic  

Example configuration:

```python
LOSS_PROBABILITY = 0.25
```

This means approximately 25% of packets are randomly dropped, forcing the protocols to recover.

---

## Example Output

```
=== Stop-and-Wait Demo ===
Sender sends packet 0
Packet 0 was LOST
Timeout waiting for ACK 0, retransmitting...

=== Go-Back-N Demo ===
Sender window: [0, 1, 2, 3]
Packet 2 was LOST
Timeout. Go-Back-N retransmits from packet 2

=== Selective Repeat Demo ===
Sender sends packet 2
Packet 2 was LOST
Only packet 2 will be retransmitted later
```

---

## Key Takeaways

- Reliable data transfer requires more than just retransmission  
- Sequence numbers prevent duplicate delivery  
- Sliding windows improve link utilization and throughput  
- Different protocols make tradeoffs between efficiency and complexity  

---

## Connection to TCP

Modern TCP combines ideas from both Go-Back-N and Selective Repeat:

- Uses cumulative acknowledgments (like GBN)  
- Buffers out-of-order data (like SR)  
- With Selective Acknowledgment (SACK), TCP can retransmit only missing segments  

This hybrid approach allows TCP to perform efficiently across a wide range of network conditions  

---

## Future Improvements

- Add visualization of packet flow and windows  
- Simulate round-trip time (RTT) and congestion control  
- Implement TCP congestion control algorithms (Slow Start, AIMD)  
- Integrate packet analysis using Wireshark  
- Extend to full TCP connection lifecycle (3-way handshake, teardown)  