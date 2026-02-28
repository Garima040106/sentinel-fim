import json
import os

from fim.config import BASELINE_FILE
from fim.hashing import hash_file

SIGNATURE_FILE = "baseline/baseline.sig"


def load_baseline():

    if not os.path.exists(BASELINE_FILE):
        return {}

    verify_integrity()

    with open(BASELINE_FILE, "r") as f:
        return json.load(f)


def save_baseline(data):

    with open(BASELINE_FILE, "w") as f:
        json.dump(data, f, indent=4)

    sign_baseline()


def sign_baseline():

    signature = hash_file(BASELINE_FILE)

    with open(SIGNATURE_FILE, "w") as f:
        f.write(signature)


def verify_integrity():

    if not os.path.exists(SIGNATURE_FILE):
        print("[WARNING] No baseline signature found")
        return

    current_hash = hash_file(BASELINE_FILE)

    with open(SIGNATURE_FILE, "r") as f:
        stored_hash = f.read()

    if current_hash != stored_hash:
        raise RuntimeError(
            "Baseline database tampering detected!"
        )
