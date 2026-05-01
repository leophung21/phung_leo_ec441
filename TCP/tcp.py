import random
import time

PACKETS = list(range(8))
LOSS_PROBABILITY = 0.25


def unreliable_send(packet):
    """
    Simulates an unreliable network.
    Sometimes packets are lost.
    """
    if random.random() < LOSS_PROBABILITY:
        print(f"Packet {packet} was LOST")
        return False
    print(f"Packet {packet} delivered")
    return True


def stop_and_wait():
    print("\n=== Stop-and-Wait Demo ===")

    for packet in PACKETS:
        ack_received = False

        while not ack_received:
            print(f"Sender sends packet {packet}")

            if unreliable_send(packet):
                print(f"Receiver sends ACK {packet}")
                ack_received = True
            else:
                print(f"Timeout waiting for ACK {packet}, retransmitting...")

            time.sleep(0.5)

    print("All packets delivered using Stop-and-Wait")


def go_back_n(window_size=4):
    print("\n=== Go-Back-N Demo ===")

    base = 0

    while base < len(PACKETS):
        window = PACKETS[base:base + window_size]
        print(f"\nSender window: {window}")

        lost = False

        for packet in window:
            print(f"Sender sends packet {packet}")

            if not unreliable_send(packet):
                lost = True
                print(f"Packet {packet} lost. Receiver discards later out-of-order packets.")
                break
            else:
                print(f"Receiver sends cumulative ACK {packet}")

        if lost:
            print(f"Timeout. Go-Back-N retransmits from packet {packet}")
        else:
            base += len(window)

        time.sleep(0.7)

    print("All packets delivered using Go-Back-N")


def selective_repeat(window_size=4):
    print("\n=== Selective Repeat Demo ===")

    base = 0
    acknowledged = set()

    while base < len(PACKETS):
        window = PACKETS[base:base + window_size]
        print(f"\nSender window: {window}")

        for packet in window:
            if packet in acknowledged:
                continue

            print(f"Sender sends packet {packet}")

            if unreliable_send(packet):
                print(f"Receiver buffers packet {packet} and sends ACK {packet}")
                acknowledged.add(packet)
            else:
                print(f"Only packet {packet} will be retransmitted later")

        while base in acknowledged:
            base += 1

        time.sleep(0.7)

    print("All packets delivered using Selective Repeat")


if __name__ == "__main__":
    random.seed(3)

    stop_and_wait()
    go_back_n()
    selective_repeat()