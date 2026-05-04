from scapy.all import IP, ICMP, TCP, sr1

print("=== Scapy Packet Lab ===")

# -------------------------
# 1. Build a basic IP + ICMP packet
# -------------------------
print("\n[1] Building ICMP Packet...")

packet = IP(dst="8.8.8.8") / ICMP()
packet.show()

# -------------------------
# 2. Send ICMP (Ping)
# -------------------------
print("\n[2] Sending ICMP Request...")

reply = sr1(packet, timeout=2, verbose=0)

if reply:
    print("Received reply:")
    reply.show()
else:
    print("No reply received")

# -------------------------
# 3. TCP SYN Scan (Port Check)
# -------------------------
print("\n[3] TCP SYN Packet...")

syn_packet = IP(dst="scanme.nmap.org") / TCP(dport=80, flags="S")

syn_reply = sr1(syn_packet, timeout=2, verbose=0)

if syn_reply:
    print("Response flags:", syn_reply.sprintf("%TCP.flags%"))
else:
    print("No response")

# -------------------------
# 4. Custom Packet with TTL
# -------------------------
print("\n[4] Custom TTL Packet...")

custom_packet = IP(dst="8.8.8.8", ttl=5) / ICMP()

reply = sr1(custom_packet, timeout=2, verbose=0)

if reply:
    print("Reply TTL:", reply.ttl)
else:
    print("No reply")

print("\n=== Lab Complete ===")
