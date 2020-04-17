#!/usr/bin/env python
import csv

with open('DATA/knights.csv') as knights_in:
    rdr = csv.reader(knights_in)
    for record in rdr:
        print(record)
print()

with open('DATA/knights.csv') as knights_in:
    rdr = csv.DictReader(knights_in, fieldnames='name title color quest comment'.split() )
    for record in rdr:
        print(record['title'], record['name'])
