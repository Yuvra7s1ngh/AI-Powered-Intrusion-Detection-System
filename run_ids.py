import joblib
import pandas as pd
from scapy.all import sniff, IP, TCP, UDP

# Load the trained model
model = joblib.load("models/ids_model.pkl")

print("[+] AI-Based Intrusion Detection System is running...")
print("[*] Waiting for packets...")


def extract_packet_features(pkt):
    # Basic checks and defaults
    if IP not in pkt:
        return None

    proto = pkt[IP].proto
    pkt_len = len(pkt)
    sport = 0
    dport = 0
    syn = 0
    ack = 0

    if TCP in pkt:
        sport = pkt[TCP].sport
        dport = pkt[TCP].dport
        syn = int(pkt[TCP].flags.S)
        ack = int(pkt[TCP].flags.A)
    elif UDP in pkt:
        sport = pkt[UDP].sport
        dport = pkt[UDP].dport

    return {
        "proto": proto,
        "pkt_len": pkt_len,
        "sport": sport,
        "dport": dport,
        "flag_SYN": syn,
        "flag_ACK": ack
    }


def packet_callback(pkt):
    features = extract_packet_features(pkt)
    if features is None:
        return  # skip packets without IP

    df = pd.DataFrame([features])

    # Make sure columns are in the same order used during training
    expected_columns = ['proto', 'pkt_len',
                        'sport', 'dport', 'flag_SYN', 'flag_ACK']
    df = df[expected_columns]

    prediction = model.predict(df)[0]

    if prediction == 1:
        print(f"[!] Intrusion Detected: {pkt.summary()}")
    else:
        print(f"[*] Normal packet: {pkt.summary()}")


# Start sniffing for packets (you can change iface="Ethernet" if needed)
sniff(prn=packet_callback, filter="ip", store=0)
