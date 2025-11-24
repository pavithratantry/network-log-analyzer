from collections import Counter
import re

# simple rules for demo. Expand as needed.
INTERFACE_FLAP_RE = re.compile(r"Interface (?P<intf>\S+) changed state to (?:down|up)", re.IGNORECASE)
BGP_RESET_RE = re.compile(r"BGP:.*reset|BGP.*flap", re.IGNORECASE)
OSPF_DROP_RE = re.compile(r"OSPF.*Neighbor.*Lost|OSPF-\d-ADJCHG", re.IGNORECASE)
CPU_HIGH_RE = re.compile(r"CPU.*(?:%|percent|utilization).*\d+", re.IGNORECASE)


def detect_anomalies(parsed_logs):
    anomalies = []
    messages = [p['message'] for p in parsed_logs if p.get('message')]

    # Interface flap detection
    ints = []
    for msg in messages:
        m = INTERFACE_FLAP_RE.search(msg)
        if m:
            ints.append(m.group('intf'))
    int_counts = Counter(ints)
    for intf, cnt in int_counts.items():
        if cnt >= 3:
            anomalies.append({'type': 'Interface Flap', 'interface': intf, 'count': cnt, 'summary': f'Interface {intf} flapped {cnt} times'})

    # OSPF drops
    ospf_events = [m for m in messages if OSPF_DROP_RE.search(m)]
    if ospf_events:
        anomalies.append({'type': 'OSPF Neighbor Down', 'count': len(ospf_events), 'message': ospf_events[:5], 'summary': f'{len(ospf_events)} OSPF adjacency events'})

    # BGP resets
    bgp_events = [m for m in messages if BGP_RESET_RE.search(m)]
    if bgp_events:
        anomalies.append({'type': 'BGP Reset/Flap', 'count': len(bgp_events), 'message': bgp_events[:5], 'summary': f'{len(bgp_events)} BGP reset events'})

    # CPU spikes (naive)
    cpu_events = [m for m in messages if CPU_HIGH_RE.search(m)]
    if cpu_events:
        anomalies.append({'type': 'High CPU', 'count': len(cpu_events), 'message': cpu_events[:3], 'summary': 'High CPU events detected'})

    return anomalies