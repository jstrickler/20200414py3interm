#!/usr/bin/env python

fruits = ["pomegranate", "cherry", "apricot", "Apple",
"lemon", "Kiwi", "ORANGE", "lime", "Watermelon", "guava",
"Papaya", "FIG", "pear", "banana", "Tamarind", "Persimmon",
"elderberry", "peach", "BLUEberry", "lychee", "GRAPE", "date" ]

f1 = sorted(fruits)
print("f1: {}\n".format(f1))

def tolower(s):
    # print("s:", s)
    return s.lower()

#                   keyfunc=
f2 = sorted(fruits, key=str.lower)
print("f2: {}\n".format(f2))

f3 = sorted(fruits, key=tolower)
print("f3: {}\n".format(f3))

f4 = sorted(fruits, key=len)
print("f4: {}\n".format(f4))

def len_and_name(f):
    return len(f), f.lower()

print(len_and_name("apple"))
print(len_and_name)

f5 = sorted(fruits, key=len_and_name)
print("f5: {}\n".format(f5))

f6 = sorted(fruits, key=lambda f: (len(f), f.lower()))
print("f6: {}\n".format(f6))


# x   function object itself
# x() return value call the function

nums = [800, -12, 80, -5, 1000, 32, 255, 400, 5, 5000, -50]
n1 = sorted(nums)
print("n1: {}\n".format(n1))

def custom_num_sort(n):
    return abs(n)

n2 = sorted(nums, key=custom_num_sort)
print("n2: {}\n".format(n2))

# lambda param, ...: return_value

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

for person in sorted(people):
    print(person)
print('-' * 60)

def by_dob(person):
    return person[3]

for person in sorted(people, key=by_dob):
    print(person)
print('-' * 60)


for person in sorted(people, key=lambda p: p[-1]):
    print(person)
print('-' * 60)

for person in sorted(people, key=lambda p: (p[3], p[1], p[0], p[2])):
    print(person)
print('-' * 60)

