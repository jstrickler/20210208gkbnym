#!/usr/bin/env python
import csv

with open('../DATA/knights.csv') as knights_in:
    rdr = csv.reader(knights_in)  # <1>
    for row in rdr:
        name, title, color, quest, comment, number, ladies = row # <2>
        print('{:4s} {:9s} {}'.format(
            title, name, quest
        ))
        print(row)
