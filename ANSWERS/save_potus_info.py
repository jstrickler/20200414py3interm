#!/usr/bin/env python
"""

@author: jstrick
Created on Wed Mar 20 23:34:17 2013

"""
import csv
import pickle
from collections import namedtuple

fields = 'term firstname lastname birthplace birthstate party'
President = namedtuple('President', fields)

presidents = []
with open('../DATA/presidents.csv') as PRES:
    rdr = csv.reader(PRES)
    for row in rdr:
        pres = President(*row)
        presidents.append(pres)

print(presidents[15].firstname, end=' ')
print(presidents[15].lastname, end=' ')
print(presidents[42].party)

with open('potus.pic','wb') as POTUS:
    pickle.dump(presidents,POTUS)
