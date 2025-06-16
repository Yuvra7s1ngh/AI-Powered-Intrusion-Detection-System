def is_private_ip(ip):
    return ip.startswith("192.") or ip.startswith("10.") or ip.startswith("172.")

def format_log(pkt_data):
    return f"[{pkt_data['src_ip']} → {pkt_data['dst_ip']}] ({pkt_data['proto']})"