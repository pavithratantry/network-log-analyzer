import re
from datetime import datetime

# Basic Cisco syslog regex (tweakable)
LOG_PATTERN = re.compile(
    r'^(?P<timestamp>[A-Za-z]{3}\s+\d+\s+\d+:\d+:\d+)\s+(?P<device>\S+)\s+(?P<message>.*)$'
)


def parse_logs(path: str):
    parsed = []
    with open(path, 'r', encoding='utf-8', errors='ignore') as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            m = LOG_PATTERN.match(line)
            if m:
                ts = m.group('timestamp')
                try:
                    # No year in syslog, use current year
                    ts_dt = datetime.strptime(f"{ts} {datetime.now().year}", "%b %d %H:%M:%S %Y")
                except Exception:
                    ts_dt = None
                parsed.append({
                    'raw': line,
                    'timestamp': ts_dt,
                    'device': m.group('device'),
                    'message': m.group('message')
                })
            else:
                # fallback: keep raw line
                parsed.append({'raw': line, 'timestamp': None, 'device': None, 'message': line})
    return parsed