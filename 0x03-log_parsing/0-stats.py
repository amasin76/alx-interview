#!/usr/bin/python3
import sys
import signal

# Initialize variables
total_size = 0
line_count = 0
status_codes = {str(i): 0 for i in [200, 301, 400, 401, 403, 404, 405, 500]}


def print_stats(signal=None, frame=None):
    print("File size: {}".format(total_size))
    for code in sorted(status_codes.keys()):
        if status_codes[code] > 0:
            print("{}: {}".format(code, status_codes[code]))


# Handle keyboard interruption
signal.signal(signal.SIGINT, print_stats)

try:
    for line in sys.stdin:
        try:
            parts = line.split()
            size = int(parts[-1])
            status_code = parts[-2]

            if status_code in status_codes:
                status_codes[status_code] += 1

            total_size += size
            line_count += 1

            if line_count % 10 == 0:
                print_stats()

        except Exception:
            continue

except KeyboardInterrupt:
    pass

finally:
    print_stats()
