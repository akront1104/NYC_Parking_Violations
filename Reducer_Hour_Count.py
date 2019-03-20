#!/usr/bin/python
import collections
import sys

# Default value: Int
result = collections.defaultdict(int)

# Input: [hour, count] from mapper
for line in sys.stdin:
    k, v = line.strip().split(',')
    result[k] += int(v)
for k, v in result.items():
    print(k, v)
