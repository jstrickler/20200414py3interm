#!/usr/bin/env python
from copy import deepcopy

x = 5  # what happens?
y = x  # ???

print(x, y)

x = 10

print(x, y)

m = None

a = "apple"
a = 5
a = 5.0
a = None
a = 5

print(a)

print(id(x), id(y), id(a))

list1 = ['a', 'b', 'c']
list2 = list1  # alias, not copy

list2.append("wombat")
print(list1)

list3 = list(list1)   # shallow copy
list4 = list1[::]     # also shallow copy

r = [['a', 'b', 'c'], [1, 2, 3, 4, 5]]
rr = list(r)  # shallow copy of r
rr.append("wombat")
print(r)
print(rr)
print()

rr[0].append("spam")
print(r)
print(rr, '\n')

rrr = deepcopy(r)
rrr[0].append('honey badger')

print(r)
print(rrr, '\n')

# var = ???

for i in range(3):
    # i =  next(range(3))
    print(i)

m = 12_323_390_381_729_382_233_323
print(m)
n = 12_34_67_78
print(n)

f = 123.456
g = 1.2093e22

print(f, g)

print(str(g))

def foo():
    pass

print(foo)
print(str(foo))

fruits = ["pomegranate", "cherry", "apricot", "apple",
"lemon", "kiwi", "orange", "lime", "watermelon", "guava",
"papaya", "fig", "pear", "banana", "tamarind", "persimmon",
"elderberry", "peach", "blueberry", "lychee", "grape", "date" ]

print(fruits[0], fruits[5], fruits[-1])
print(fruits[:4])  # fruits[0:4]
print(fruits[-3:])  # fruits[-3:len(fruits)]
print(fruits[4:10])
print(fruits[:])
print(len(fruits))

d1 = dict()
d2 = {}
months = {'Jan': 31, "Feb": 28, "Mar": 31}
print(months['Jan'])
for month in 'Jan', 'Mar', 'Oct', 'Dec':
    print(month, months.get(month))

for month in 'Jan', 'Mar', 'Oct', 'Dec':
    print(month, months.get(month, "NOT FOUND"))
print()

#    k      v        d
for month, days in months.items():
    print(month, days)

print(months.keys())
print(months.values(), '\n')

set1 = {'Python', 'Perl', 'COBOL', 'Kotlin'}
set2 = {'Lua', 'Go', 'Python', 'Perl', 'Java'}

print(set1 & set2)  # intersection
print(set1 | set2)  # union
print(set1 ^ set2)  # xor
print(set1 - set2)  # diff
print(set2 - set1)  # diff

print(list(months))
print(list(months.items()))

# for m, d in months:  # will not work
#     print(m, d)

