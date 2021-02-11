#!/usr/bin/env python

import sys
import os

if len(sys.argv) < 2:
    start_dir = "."
else:
    start_dir = sys.argv[1]

for base_name in os.listdir(start_dir):  # <1>
    file_name = os.path.join(start_dir, base_name)
    if os.access(file_name, os.W_OK | os.X_OK | os.R_OK):  # <2>
        print(file_name, "is writable")
    print("\t", os.stat(file_name))
    print("\t", os.path.getsize(file_name))
    print("\t", os.path.getmtime(file_name)) # datetime.datetime.fromtimestamp(t)