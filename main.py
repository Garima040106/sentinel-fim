import sys
import os
import time
from watchdog.observers import Observer

from fim.monitor import FIMHandler
from fim.config import WATCHED_DIRECTORIES
from fim.hashing import calculate_hash
from fim.database import save_baseline


def initialize_baseline():

    baseline = {}

    print("[*] Creating baseline...")

    for directory in WATCHED_DIRECTORIES:
        for root, _, files in os.walk(directory):

            for file in files:
                path = os.path.join(root, file)

                file_hash = calculate_hash(path)

                if file_hash:
                    baseline[path] = file_hash

    save_baseline(baseline)

    print("[✓] Baseline created successfully")


def start_monitoring():

    observer = Observer()
    handler = FIMHandler()

    for directory in WATCHED_DIRECTORIES:
        observer.schedule(handler, directory, recursive=True)

    observer.start()

    print("Sentinel FIM running...")

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()

    observer.join()


if __name__ == "__main__":

    if "--init" in sys.argv:
        initialize_baseline()
    else:
        start_monitoring()
