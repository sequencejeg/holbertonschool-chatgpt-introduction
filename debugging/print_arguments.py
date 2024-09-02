#!/usr/bin/python3
import sys

if len(sys.argv) > 1:
    for i in range(1, len(sys.argv)):  # Skip the script name
        print(sys.argv[i])
else:
    print("No additional arguments provided.")
