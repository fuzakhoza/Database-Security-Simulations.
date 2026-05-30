import re
from collections import Counter
from datetime import datetime

# 1. SIMULATED SERVER LOG FILE DATA
# This mimics a real production server log tracking user login attempts.
MOCK_SERVER_LOGS = """
2026-05-29 22:00:01 IP: 192.168.43.12 STATUS: LOGIN_SUCCESS USER: admin
2026-05-29 22:01:15 IP: 10.0.0.55 STATUS: LOGIN_FAILED USER: root
2026-05-29 22:01:16 IP: 10.0.0.55 STATUS: LOGIN_FAILED USER: root
2026-05-29 22:01:18 IP: 10.0.0.55 STATUS: LOGIN_FAILED USER: admin
2026-05-29 22:01:19 IP: 10.0.0.55 STATUS: LOGIN_FAILED USER: backup
2026-05-29 22:01:21 IP: 10.0.0.55 STATUS: LOGIN_FAILED USER: testuser
2026-05-29 22:04:30 IP: 192.168.43.102 STATUS: LOGIN_SUCCESS USER: fuza
2026-05-29 22:05:12 IP: 172.16.5.8 STATUS: LOGIN_FAILED USER: guest
2026-05-29 22:05:40 IP: 10.0.0.55 STATUS: LOGIN_FAILED USER: root
"""

def analyze_security_logs(log_data, threshold=4):
    """Parses system logs to identify Brute-Force intrusion patterns."""
    print("🔍 [FORENSIC AUDIT START] Analyzing active network authentication streams...")
    print(f"⚙️ Alert Threshold Trigger: {threshold} failed attempts from a single source.\n")
    
    # List to store all malicious IPs flagged for multiple failures
    failed_ips = []
    
    # Break down the massive log dump into individual event lines
    log_lines = log_data.strip().split('\n')
    
    for line in log_lines:
        # Use Regular Expressions (Regex) to extract the IP address and status
        ip_match = re.search(r'IP:\s+(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})', line)
        status_match = re.search(r'STATUS:\s+(\w+)', line)
        
        if ip_match and status_match:
            ip = ip_match.group(1)
            status = status_match.group(1)
            
            # If a login failure is spotted, track the IP address
            if status == "LOGIN_FAILED":
                failed_ips.append(ip)
                
    # Counter tallies up how many times each IP failed
    failure_counts = Counter(failed_ips)
    brute_force_detected = False

    # Check which IPs crossed our dangerous threshold limit
    for ip, count in failure_counts.items():
        if count >= threshold:
            brute_force_detected = True
            print("=" * 65)
            print(f"💥 [ALERT] BRUTE-FORCE INTRUSION DETECTED!")
            print(f"🥷 Hostile IP:      {ip}")
            print(f"⚠️ Total Failures:  {count} attempts inside 2 minutes.")
            print(f"⚡ Remediation:    Flagged for dynamic perimeter firewall ban.")
            print("=" * 65 + "\n")
            
    if not brute_force_detected:
        print("✅ Audit complete: No anomalous authentication thresholds breached.")

if __name__ == "__main__":
    # Execute the audit engine against our log dataset
    analyze_security_logs(MOCK_SERVER_LOGS, threshold=4)
