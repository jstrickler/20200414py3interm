#!/usr/bin/env python
#
from dateutil import parser

date_strings = [  # <1>
    'April 1, 2015',
    '4/1/2015',
    'Apr 1, 2015',
    'Apr 1 2015',
    'September 22nd 1952 12:45 PM',
    '04/01/2015',
    '1 Apr 2015',
    'April 1st, 2015',
    'April 1, 2015 8:09',
    'Feb 29, 2019',
    'September 98, 2018',
    '4/4/1944',
    '4/1/2015 8:09 PM',
    'Apr 1, 2015 5 AM',
    'October 31st, 1956',
    'Apricot 4, 341',
]

foo = [1, 2, 3]

for date_string in date_strings:
    try:
        dt = parser.parse(date_string)  # <2>
        print(dt)
    except ValueError as err:
        print("Can't parse", date_string)
