#!/usr/bin/env python
import re
import fileinput
import argparse

parser = argparse.ArgumentParser(description="Faux grep utility")

parser.add_argument('-i', action="store_true", dest="ignore_case", help="ignore_case")
parser.add_argument('-f', action="store_true", dest="show_name", help="display file name")
parser.add_argument('-n', action="store_true", dest="show_line_numbers", help="show line numbers")

parser.add_argument('pattern', help="pattern to find")

parser.add_argument('files', nargs="*", help="files to search")


args = parser.parse_args()   # process sys.argv

if args.ignore_case:
    flag = re.IGNORECASE
else:
    flag = 0  # "re.NONE"

rx_term = re.compile(args.pattern, flag)

for line in fileinput.input(args.files):
    if fileinput.isfirstline():
        line_number = 1
    if rx_term.search(line):
        if args.show_name:
            print(fileinput.filename(), end=' ')
        if args.show_line_numbers:
            print(f"{line_number}:", end=' ')
        print(line.rstrip())
    line_number += 1
