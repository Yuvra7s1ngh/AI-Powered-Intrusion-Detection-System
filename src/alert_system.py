def alert_user(pkt_data):
    print("\n🚨 Alert: Intrusion Detected!")
    print(f"[!] Source IP: {pkt_data['src_ip']} → Destination IP: {pkt_data['dst_ip']}")
    print(f"[!] Protocol: {pkt_data['proto']}, Length: {pkt_data['pkt_len']}")