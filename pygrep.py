import fileinput
import argparse

parser = argparse.ArgumentParser(description="Faux grep")

parser.add_argument("-i", dest="ignore_case", action="store_true", help="Ignore case")
parser.add_argument("-f", dest="show_file_name", action="store_true", help="Show file name")
parser.add_argument("-n", dest="show_line_numbers", action="store_true", help="Show line numbers")
parser.add_argument("pattern", help="Pattern to find")
parser.add_argument("files", nargs="*", help="Files to search")

args = parser.parse_args()  # parse sys.argv, args.ignore_case
if args.ignore_case:
    args.pattern = args.pattern.lower()

line_number = 1
for raw_line in fileinput.input(args.files):
    if fileinput.isfirstline():
        line_number = 1
    orig_line = raw_line.rstrip()
    if args.ignore_case:
        line_to_check = orig_line.lower()
    else:
        line_to_check = orig_line
    if args.pattern in line_to_check:
        line = raw_line.rstrip()  # remove \n
        if args.show_file_name:
            print(fileinput.filename(), end=': ')
        if args.show_line_numbers:
            print("{}:".format(line_number), end=' ')
        print(line)
    line_number += 1