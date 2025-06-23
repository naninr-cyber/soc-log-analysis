# log_parser.py

# This script analyzes a Linux authentication log (auth.log)
# and extracts failed login attempts with usernames and IPs.

import re

# Log file to read — replace this with your actual log file path if needed
log_file_path = "sample-auth.log"

# Pattern to match "Failed password" lines (SSH login failures)
pattern = r"Failed password for (invalid user )?(\w+) from ([\d.]+) port"

try:
    with open(log_file_path, "r") as file:
        lines = file.readlines()
    
    print("🔍 Failed Login Attempts:\n")
    count = 0

    for line in lines:
        match = re.search(pattern, line)
        if match:
            user = match.group(2)
            ip = match.group(3)
            print(f"User: {user.ljust(12)} | IP: {ip}")
            count += 1

    if count == 0:
        print("No failed login attempts found.")
    else:
        print(f"\nTotal failed login attempts: {count}")

except FileNotFoundError:
    print(f"❌ Log file not found: {log_file_path}")
except Exception as e:
    print(f"❗ Error occurred: {e}")
