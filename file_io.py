#!/usr/bin/env python

with open('DATA/mary.txt') as mary_in:    # mary_in = open(....)
    for raw_line in mary_in:
        line = raw_line.rstrip() # remove \n
        print(line)

fruits = ["pomegranate", "cherry", "apricot", "apple",
"lemon", "kiwi", "orange", "lime", "watermelon", "guava",
"papaya", "fig", "pear", "banana", "tamarind", "persimmon",
"elderberry", "peach", "blueberry", "lychee", "grape", "date" ]

with open('fruits.txt', 'w') as fruits_out:
    for f in fruits:
        fruits_out.write(f + '\n')

