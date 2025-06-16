import pandas as pd

def preprocess_packets(packet_list):
    df = pd.DataFrame(packet_list)
    df.fillna(0, inplace=True)
    df['flags'] = df['flags'].astype(str)
    df['flag_SYN'] = df['flags'].apply(lambda x: 1 if 'S' in x else 0)
    df['flag_ACK'] = df['flags'].apply(lambda x: 1 if 'A' in x else 0)
    df.drop(['flags'], axis=1, inplace=True)
    return df