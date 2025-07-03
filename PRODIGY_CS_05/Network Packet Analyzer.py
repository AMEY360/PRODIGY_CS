from scapy.all import sniff, IP, TCP, UDP, Raw
from datetime import datetime

def process_packet(packet):
    print("=====================================")
    print(f"📅 Time: {datetime.now()}")

    if IP in packet:
        ip_layer = packet[IP]
        print(f"📤 Source IP: {ip_layer.src}")
        print(f"📥 Destination IP: {ip_layer.dst}")
        print(f"🌐 Protocol: {ip_layer.proto}")

        if TCP in packet:
            print("🔧 TCP Packet")
            print(f"Source Port: {packet[TCP].sport}")
            print(f"Destination Port: {packet[TCP].dport}")
        elif UDP in packet:
            print("🔧 UDP Packet")
            print(f"Source Port: {packet[UDP].sport}")
            print(f"Destination Port: {packet[UDP].dport}")
        
        if Raw in packet:
            payload = packet[Raw].load
            print(f"📦 Payload (raw data): {payload[:50]}")  # limit payload view
    else:
        print("Non-IP Packet detected.")

def main():
    print("📡 Starting Packet Sniffer (Press Ctrl+C to stop)...")
    # Requires administrative/root privileges
    sniff(filter="ip", prn=process_packet, store=False)

if __name__ == "__main__":
    main()
