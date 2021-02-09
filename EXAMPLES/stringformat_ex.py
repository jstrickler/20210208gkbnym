#!/usr/bin/env python

from datetime import date

color = 'blue'
animal = 'iguana'

print('{} {}'.format(color, animal))  # <1>

fahr = 98.6839832
print('{:.1f}'.format(fahr))  # <2>

value = 12345
print('{0:d} {0:04x} {0:08o} {0:016b}'.format(value))  # <3>

data = {'apple': 38, 'kiwi': 127, 'apricot': 9}

for letter, number in sorted(data.items()):
    print("{:8s} {:4d}".format(letter, number))  # <4>
