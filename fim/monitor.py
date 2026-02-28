from watchdog.events import FileSystemEventHandler
import os

from fim.hashing import calculate_hash
from fim.database import load_baseline, save_baseline
from fim.alerts import log_alert


baseline = load_baseline()


class FIMHandler(FileSystemEventHandler):

    def process(self, filepath):

        if not os.path.isfile(filepath):
            return

        new_hash = calculate_hash(filepath)
        old_hash = baseline.get(filepath)

        if old_hash is None:
            baseline[filepath] = new_hash
            log_alert(f"New file detected: {filepath}")

        elif old_hash != new_hash:
            baseline[filepath] = new_hash
            log_alert(f"File modified: {filepath}")

        save_baseline(baseline)

    def on_created(self, event):
        self.process(event.src_path)

    def on_modified(self, event):
        self.process(event.src_path)

    def on_deleted(self, event):
        log_alert(f"File deleted: {event.src_path}")
