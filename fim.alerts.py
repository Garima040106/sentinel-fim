from datetime import datetime
from fim.config import LOG_FILE


def log_alert(message):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open(LOG_FILE, "a") as f:
        f.write(f"[{timestamp}] {message}\n")

    print(f"[ALERT] {message}")
