import json
from datetime import datetime

FORENSIC_LOG = "logs/forensic_log.json"


def log_event(event_type, filepath, severity):

    event = {
        "timestamp": datetime.now().isoformat(),
        "event_type": event_type,
        "file": filepath,
        "severity": severity
    }

    try:
        with open(FORENSIC_LOG, "a") as f:
            json.dump(event, f)
            f.write("\n")
    except Exception as e:
        print("Forensic logging failed:", e)
