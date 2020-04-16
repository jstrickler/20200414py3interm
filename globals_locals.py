#!/usr/bin/env python

animal = "wombat"

def spam():
    m = "wolverine"  # 'm' is local name
    animal = "honey badger"
    print("in spam: local animal:", animal)
    print("in spam: global animal:", globals()['animal'])
    print("in spam: all local names:", locals())
    return m

x = spam()

print(x)

g = globals()

print(g, '\n')

print(x, g['x'])

a = 10
b = a

g["color"] = "purple"

print(color)  # same as     color = "purple"

