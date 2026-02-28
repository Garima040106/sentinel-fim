from datetime import datetime
from colorama import Fore, Style, init
from fim.config import LOG_FILE
from fim.forensics import log_event

init(autoreset=True)


def log_alert(message, severity="LOW", filepath="unknown"):

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    color = Fore.GREEN

    if severity == "MEDIUM":
        color = Fore.YELLOW
    elif severity == "HIGH":
        color = Fore.RED
    elif severity == "CRITICAL":
        color = Fore.MAGENTA

    log_line = f"[{timestamp}] [{severity}] {message}"

    with open(LOG_FILE, "a") as f:
        f.write(log_line + "\n")

    print(color + log_line + Style.RESET_ALL)

    log_event(message, filepath, severity)
