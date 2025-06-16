from scapy.all import sniff

print("Starting packet sniffing for 10 packets...")


def packet_callback(pkt):
    print(pkt.summary())


sniff(count=10, prn=packet_callback)

print("Finished sniffing.")
