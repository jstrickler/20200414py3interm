#!/usr/bin/env python

fruits = ["pomegranate", "cherry", "apricot", "apple",
"lemon", "kiwi", "orange", "lime", "watermelon", "guava",
"papaya", "fig", "pear", "banana", "tamarind", "persimmon",
"elderberry", "peach", "blueberry", "lychee", "grape", "date" ]

f0 = []
for f in fruits:
    f0.append(f.upper())
print("f0: {}\n".format(f0))

f1 = [f.upper() for f in fruits]  # list comprehension
print("f1: {}\n".format(f1))

# SILLY!!
x1 = ["wombat" for f in fruits]
print("x1: {}\n".format(x1))

f2 = [f.upper() for f in fruits if f.startswith('p')]
print("f2: {}\n".format(f2))

f3 = [f for f in fruits if f.startswith('p')]
print("f3: {}\n".format(f3))

nums = [800.2, 80, 1000.0, 32, 255, 400, 5.7, 5000]

n1 = [i/2 for i in nums]
print("n1: {}\n".format(n1))

n2 = [int(i) for i in nums]
print("n2: {}\n".format(n2))

values = [72.3, 69.1, 76, 76.0, 79]

v1 = [int(v) for v in values]
print(v1)
c1 = [chr(v) for v in v1]
print(c1)

print("".join(c1))

c2 = [chr(int(v)) for v in values]
print(c2, '\n')

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

last_names = [p[1] for p in people]
print("last_names: {}\n".format(last_names))

full_names = ["{} {}".format(p[0], p[1]) for p in people]
print("full_names: {}\n".format(full_names))
