from watchdog.observers import Observer
import time

from fim.monitor import FIMHandler
from fim.config import WATCHED_DIRECTORIES


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
    start_monitoring()
