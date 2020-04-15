#!/usr/bin/env python


letters = "pdq"


place = 55.32, 102.34

lat, lon = place

print(place)
print(lat, lon)

a, b, c = letters
print(a)
print(b)
print(c)

lat, lon = 55.32, 102.34

values = ['a', 'b', 'c', 'd', 'e', 'f']

x, y, *z = values
print(x, y, z)
x, *y, z = values
print(x, y, z)
*x, y, z = values
print(x, y, z)




