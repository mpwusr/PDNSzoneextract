#!/usr/bin/env python3
import csv
import sys

def zone_to_csv(zone_file, csv_file):
    with open(zone_file, 'r') as zf, open(csv_file, 'w', newline='') as cf:
        writer = csv.writer(cf)
        # CSV headers
        writer.writerow(['Name', 'TTL', 'Type', 'Content'])
        for line in zf:
            # Skip empty lines or comments
            if not line.strip() or line.startswith(';'):
                continue
            # Split zone file line into components (name, ttl, class, type, content)
            parts = line.split()
            if len(parts) >= 4:  # Ensure it’s a valid record
                name, ttl, _, rtype = parts[0:4]
                content = ' '.join(parts[4:])
                writer.writerow([name, ttl, rtype, content])

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python zone_to_csv.py <zone_file> <csv_file>")
        sys.exit(1)
    zone_to_csv(sys.argv[1], sys.argv[2])