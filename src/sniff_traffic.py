from scapy.all import sniff, IP, TCP, UDP
from src.feature_engineering import preprocess_packets
from src.predict import detect_intrusion
from src.alert_system import alert_user


def process_packet(pkt):
    if IP in pkt:
        pkt_data = {
            'src_ip': pkt[IP].src,
            'dst_ip': pkt[IP].dst,
            'proto': pkt.proto,
            'pkt_len': len(pkt),
            'sport': pkt[TCP].sport if TCP in pkt else (pkt[UDP].sport if UDP in pkt else 0),
            'dport': pkt[TCP].dport if TCP in pkt else (pkt[UDP].dport if UDP in pkt else 0),
            'flags': pkt.sprintf('%TCP.flags%') if TCP in pkt else '',
        }
        result = detect_intrusion(pkt_data)
        if result == 1:
            alert_user(pkt_data)


def start_sniffing():
    sniff(prn=packet_callback, filter="ip", store=0, timeout=60)
