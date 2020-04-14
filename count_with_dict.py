#!/usr/bin/env python

fruits = ["pomegranate", "cherry", "apricot", "apple",
"lemon", "kiwi", "orange", "lime", "watermelon", "guava",
"papaya", "fig", "pear", "banana", "tamarind", "persimmon",
"elderberry", "peach", "blueberry", "lychee", "grape", "date" ]

counts = {}

for fruit in fruits:
    first = fruit[0]
    if first not in counts:
        counts[first] = 0

    counts[first] += 1  # counts[first] = counts[first] + 1

print(counts)
