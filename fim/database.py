import json
import os
from fim.config import BASELINE_FILE


def load_baseline():
    if not os.path.exists(BASELINE_FILE):
        return {}

    with open(BASELINE_FILE, "r") as f:
        return json.load(f)


def save_baseline(data):
    with open(BASELINE_FILE, "w") as f:
        json.dump(data, f, indent=4)
