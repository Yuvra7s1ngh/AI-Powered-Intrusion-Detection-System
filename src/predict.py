import joblib
from src.feature_engineering import preprocess_packets

model = joblib.load("models/ids_model.pkl")

def detect_intrusion(pkt_data):
    df = preprocess_packets([pkt_data])
    prediction = model.predict(df)
    return prediction[0]  # 0 = normal, 1 = attack