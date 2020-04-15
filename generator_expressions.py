#!/usr/bin/env python

letters = ['alpha', 'beta', 'gamma']

e = enumerate(letters)
for i, letter in e:
    print(i, letter)
print('-' * 60)

e = enumerate(letters)
print(next(e))
print(next(e))
print()

with open('DATA/mary.txt') as mary_in:
    next(mary_in)
    for raw_line in mary_in:
        print(raw_line.rstrip())
print()

iletters = iter(letters)
print(next(iletters))
print(next(iletters))

fruits = ["pomegranate", "cherry", "apricot", "apple",
"lemon", "kiwi", "orange", "lime", "watermelon", "guava",
"papaya", "fig", "pear", "banana", "tamarind", "persimmon",
"elderberry", "peach", "blueberry", "lychee", "grape", "date" ]

f1 = (f.upper() for f in fruits)  # generator expression
print("f1: {}\n".format(f1))
for fruit in f1:
    print(fruit)
print('-' * 60)

people = [
    ('Melinda', 'Gates', 'Gates Foundation', '1964-08-15'),
    ('Steve', 'Jobs', 'Apple', '1955-02-24'),
    ('Larry', 'Wall', 'Perl', '1954-09-27'),
    ('Paul', 'Allen', 'Microsoft', '1953-01-21'),
    ('Larry', 'Ellison', 'Oracle', '1944-08-17'),
    ('Bill', 'Gates', 'Microsoft', '1955-10-28'),
    ('Mark', 'Zuckerberg', 'Facebook', '1984-05-14'),
    ('Sergey','Brin', 'Google', '1973-08-21'),
    ('Larry', 'Page', 'Google', '1973-03-26'),
    ('Linus', 'Torvalds', 'Linux', '1969-12-28'),
]

last_names = (p[1] for p in people) # generator expression

for last_name in last_names:
    print(last_name)
print()



























