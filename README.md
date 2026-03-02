# Sentinel FIM 🛡️

### Real-Time File Integrity Monitoring & Behavioral Threat Detection for Linux
![Python](https://img.shields.io/badge/Python-3.x-blue)
![Platform](https://img.shields.io/badge/Platform-Linux-green)
![Security](https://img.shields.io/badge/Domain-Cybersecurity-red)
![Status](https://img.shields.io/badge/Status-Active-success)
![License](https://img.shields.io/badge/License-MIT-yellow)
Sentinel is a lightweight host-based security tool that monitors filesystem activity in real time and detects unauthorized or suspicious system changes.

The project was built to explore how modern endpoint protection and intrusion detection systems verify system integrity and detect early signs of compromise such as file tampering or ransomware-like behavior.

---
# Sentinel FIM 🛡️

(short project intro)

## 🎬 Live Demonstration

![Sentinel Demo](docs/demo.gif)

## 🧭 Architecture

```mermaid
flowchart TD

A[Linux Filesystem Events]
--> B[Watchdog Observer]

B --> C[Sentinel Monitoring Engine]

C --> D[Hash Engine<br>SHA256 Verification]
C --> E[Behavior Engine<br>Ransomware Detection]

D --> F[Threat Classification]
E --> F

F --> G[Alert System]
G --> H[Forensic Logger<br>JSON Logs]
## 🚀 Features

* Real-time file monitoring using filesystem events
* Cryptographic file integrity verification (SHA-256)
* Trusted baseline creation and validation
* Baseline tamper detection
* Threat severity classification
* Behavioral detection for rapid file modification activity
* JSON forensic logging for incident analysis
* Linux background service support (systemd)

---

## 🧠 How It Works

Sentinel follows a trust-based monitoring model:

1. A trusted **baseline snapshot** of monitored files is created.
2. Each file is hashed using SHA-256.
3. Filesystem events are monitored continuously.
4. Any change is verified against the trusted baseline.
5. Suspicious activity patterns trigger elevated alerts.

If the baseline itself is modified, Sentinel detects possible tampering and stops execution to prevent false trust.

---

## ⚙️ Installation

Clone the repository:

```
git clone https://github.com/Garima040106/sentinel-fim.git
cd sentinel-fim
```

Create environment:

```
python3 -m venv cyenv
source cyenv/bin/activate
pip install -r requirements.txt
```

---

## 🧩 Initialize Trusted Baseline

```
python main.py --init
```

---

## ▶️ Run Sentinel

```
python main.py
```

---

## 🔍 Example Alerts

```
[LOW] New file detected
[HIGH] File modified
[CRITICAL] File deleted
[CRITICAL] Possible ransomware behavior detected
```

---

## 📂 Project Structure

```
sentinel-fim/
│
├── fim/
│   ├── monitor.py
│   ├── hashing.py
│   ├── database.py
│   ├── alerts.py
│   ├── behavior.py
│   └── forensics.py
│
├── logs/
├── baseline/
├── main.py
└── requirements.txt
```

---

## 🛠️ Technologies Used

* Python
* Watchdog (filesystem monitoring)
* SHA-256 hashing
* Linux systemd services

---

## 🎯 Learning Goals

This project demonstrates concepts used in:

* Host Intrusion Detection Systems (HIDS)
* Endpoint Detection & Response (EDR)
* File Integrity Monitoring
* Incident Forensics
* Defensive Security Engineering

---

## ⚠️ Disclaimer

Sentinel is an educational cybersecurity project intended for research and learning purposes. It should not replace production security solutions.

---

## 👩‍💻 Author

Garima Varma
Cybersecurity Undergraduate | Builder | Security Enthusiast
