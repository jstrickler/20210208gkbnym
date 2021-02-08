
with open('DATA/mary.txt') as mary_in:
    for raw_line in mary_in:
        line = raw_line.rstrip()
        print(line)
print('-' * 60)

with open('DATA/mary.txt') as mary_in:
    all_the_text = mary_in.read()
    print("RAW:")
    print(repr(all_the_text))
    print("NORMAL:")
    print(all_the_text)
print('-' * 60)

with open('DATA/mary.txt') as mary_in:
    all_lines_with_nl = mary_in.readlines()
    print(all_lines_with_nl)
print('-' * 60)

with open('DATA/mary.txt') as mary_in:
    all_lines_without_nl = mary_in.read().splitlines()
    print(all_lines_without_nl)
print('-' * 60)

with open("DATA/mary.txt") as mary_in:
    with open('upper_mary.txt', 'w') as mary_out:
        for line in mary_in:
            mary_out.write(line.upper())

file_name = input("Enter file to read ")
with open(file_name) as file_in:
    for raw_line in file_in:
        line = raw_line.rstrip()
        print(line)
    # file_in.close()

import sqlite3
with sqlite3.connect("somefile.db") as db:
    pass
