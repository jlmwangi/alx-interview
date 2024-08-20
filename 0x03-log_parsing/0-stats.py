#!/usr/bin/python3
''' a script thats meant to read from stdin'''

import sys
import re
import signal


pattern = re.compile(r'^\d{1,3}(\.\d{1,3}){3} - \[\d{2}/\w{3}/\d{4}(:\d{2}){3} \+\d{4}\] "GET /projects/260 HTTP/1\.1" \d{3} \d+$')
line_count = 0
sum_size = 0
status_codes = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}


def print_summary():
    """print file size and status code counts"""
    print(f'File size: {sum_size}')
    for code in sorted(status_codes.keys()):
        if status_codes[code] > 0:
            print(f"{code}: {status_codes[code]}")


def signal_handler(sig, frame):
    '''handle the SIGINT signal'''
    print_summary()
    sys.exit(0)


# register the signal handler for SIGINT
signal.signal(signal.SIGINT, signal_handler)

try:
    for line in sys.stdin:
        line_count += 1

        if not pattern.match(line):
            continue  # if line does not match, skip it

        '''Extract the file size'''
        parts = line.split()
        file_size = int(parts[-1])
        sum_size += file_size

        '''Extract the status code'''
        status_code = int(parts[-2])
        if status_code in status_codes:
            status_codes[status_code] += 1

        '''print summary every 10 lines'''
        if line_count % 10 == 0:
            print_summary()

except KeyboardInterrupt:
    print_summary()
    sys.exit(0)
