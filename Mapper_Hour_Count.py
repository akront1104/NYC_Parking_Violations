#!/usr/bin/python
"""Mapper: emits tuples in the form (hour = [0,..,24], 1)
"""
import sys
import re
for line in sys.stdin:
    if re.search('^\d', line):  # if line starts with a digit
        record = line.strip().split(',')
        ticket_time = record[19]
        try:
            hour = int(ticket_time[:2])
        except:
            continue
        if ticket_time[-1] == 'P':
            hour += 12
        print('{},{}'.format(hour, 1))
