import time
from collections import deque

# time window in seconds
EVENT_WINDOW = 10

# number of events triggering suspicion
THRESHOLD = 5

event_times = deque()


def record_event():
    now = time.time()
    event_times.append(now)

    # remove old events
    while event_times and now - event_times[0] > EVENT_WINDOW:
        event_times.popleft()


def suspicious_activity():
    return len(event_times) >= THRESHOLD
