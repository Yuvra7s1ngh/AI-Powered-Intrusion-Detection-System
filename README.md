![Build Status](https://github.com/Yuvra7s1ngh/AI-Powered-Intrusion-Detection-System/actions/workflows/python-app.yml/badge.svg)


# 🛡️ AI-Powered Intrusion Detection System for Home Networks

A real-time intrusion detection system (IDS) that leverages artificial intelligence and machine learning to monitor and analyze live network traffic on home or small office networks. This project replaces traditional static rule-based detection with dynamic AI-driven classification to detect anomalies, zero-day attacks, and malicious traffic effectively.

---

## 🚀 Features

- Real-time packet sniffing using Scapy
- AI/ML-based detection with a trained Random Forest classifier
- Lightweight and suitable for home/small office networks
- Detects unknown and zero-day network attacks
- Customizable and extensible

---

## ▶️ Getting Started

### Prerequisites

- Python 3.8 or higher
- Windows/Linux/MacOS with administrative privileges (for packet sniffing)

### Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/Yuvra7s1ngh/AI-Powered-Intrusion-Detection-System.git
    cd AI-Powered-Intrusion-Detection-System
    ```

2. Install required Python packages:
    ```bash
    pip install -r requirements.txt
    ```

---

## ▶️ How to Use

1. **Train the model** (optional if you want to retrain):
    ```bash
    python src/train_model.py
    ```

2. **Run the IDS** to start real-time packet monitoring and intrusion detection:
    ```bash
    python run_ids.py
    ```

3. **Test packet sniffing** (to verify setup):
    ```bash
    python test_sniff.py
    ```

---

## 📈 Role of AI & ML

This project uses machine learning (Random Forest classifier) to analyze network traffic features extracted in real-time, classify normal vs malicious packets, and detect previously unseen attack patterns. The AI-driven approach enhances detection accuracy beyond traditional signature-based systems.

---

## 🛠️ Tech Stack

- Python 3
- Scapy (for packet sniffing)
- scikit-learn (machine learning)
- pandas, numpy (data processing)
- joblib (model serialization)

---

## 📄 License

MIT License © Yuvraj Singh

---

Feel free to contribute or raise issues!

---
