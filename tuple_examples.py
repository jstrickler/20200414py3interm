#!/usr/bin/env python

# tuple == Struct == Record !!

person = 'Bill', 'Gates', 'Microsoft', '1955-10-22'

# person = ('Bill', 'Gates', 'Microsoft', '1955-10-22')

thing = 5,   # tuple with one element

other_thing = ()   # empty tuple

print(type(person), len(person))

print(person[0], person[3], person[-2])

print(person[0:2])

print(person.index('Bill'), person.index('Gates'))

first_name, last_name, product, dob = person

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

for person in people:
    # person = NEXT element of people
    print(person[0], person[1])
print('-' * 60)

for first_name, last_name, product, dob in people:
    # first_name, last_name, product, dob = NEXT element of people
    print(last_name, dob)
print('-' * 60)

data = [('A', 6), ('M', 14), ('K', 9)]

for letter, number in data:
    print(letter * number)
print('-' * 60)

airports = {
    'EWR': 'Newark',
    'YYZ': 'Toronto',
    'MCI': 'Kansas City',
    'SFO': 'San Francisco',
    'RDU': 'Raleigh-Durham',
    'SJC': 'San Jose',
    'MCO': 'Orlando',
    'YCC': 'Calgary',
    'ABQ': 'Albuquerque',
    'OAK': 'Oakland',
    'SMF': 'Sacramento',
    'YOW': 'Ottawa',
    'IAD': 'Dulles',
}

# GOOD PRACTICE
for abbr, name in airports.items():
    if "C" in abbr:
        print(abbr, name)
print('-' * 60)

print(list(airports.items()))
print()

print("person:", person)
for i, value in enumerate(person):
    print(i, value)
print()

print(list(enumerate(person)))
print()

# BAD PRACTICE
# for whatever in airports:
#     print(whatever, airports[whatever])
# print()

# airports.keys()  airports.values()


x = 'alpha', 'beta', 'gamma', 'delta'
e = enumerate(x)
print(e)
print(list(e))

e = enumerate(x, 100)
print(e)
print("round one:", list(e))
print("round two:", list(e))

e = enumerate(x, 100)
for i, letter in e:
    print(i, letter)
print()

r = reversed(x)
print(r)
for letter in r:
    print(letter)
print()

for i, letter in enumerate(reversed(x)):
    print(i, letter)
