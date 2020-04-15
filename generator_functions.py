#!/usr/bin/env python

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

def last_names():
    for person in people:
        yield person[1]

last_name_gen = last_names()

for last_name in last_name_gen:
    # last_name = next(last_name_gen)
    print(last_name)
print()

def trim_newline(file_name):
    with open(file_name) as file_in:
        for line in file_in:
            yield line.rstrip() # remove \n

mary = trim_newline('DATA/mary.txt')

for line in mary:
    # line = next(mary)  --> go to next 'yield'
    print(line)





