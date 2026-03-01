from watchdog.events import FileSystemEventHandler
import os

from fim.hashing import calculate_hash
from fim.database import load_baseline, save_baseline
from fim.alerts import log_alert
from fim.behavior import record_event, suspicious_activity


class FIMHandler(FileSystemEventHandler):

    def __init__(self):
        super().__init__()
        # Baseline is loaded ONLY when handler starts
        self.baseline = load_baseline()

    def process(self, filepath):

        if not os.path.isfile(filepath):
            return

        new_hash = calculate_hash(filepath)
        old_hash = self.baseline.get(filepath)

        # New File Detection
        if old_hash is None:
            self.baseline[filepath] = new_hash

            log_alert(
                "New file detected",
                severity="LOW",
                filepath=filepath
            )

        # File Modification Detection
        elif old_hash != new_hash:

            self.baseline[filepath] = new_hash

            record_event()

            if suspicious_activity():
                log_alert(
                    "Possible ransomware behavior detected",
                    severity="CRITICAL",
                    filepath=filepath
                )
            else:
                log_alert(
                    "File modified",
                    severity="HIGH",
                    filepath=filepath
                )

        save_baseline(self.baseline)

    def on_created(self, event):
        self.process(event.src_path)

    def on_modified(self, event):
        self.process(event.src_path)

    def on_deleted(self, event):

        log_alert(
            "File deleted",
            severity="CRITICAL",
            filepath=event.src_path
        )
