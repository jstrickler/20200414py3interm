#!/usr/bin/env python
from struct import Struct

# obj = ClassName(args...)
s = Struct("HIHHI")   #  Struct s = new Struct("HIHHI");

print(dir(s))

binary_stream = s.pack(5, 2332, 183, 2909, 41)

print(binary_stream)

x = 123456
print(type(x))
print(dir(x))

print(x.numerator)
print(x.bit_length())

# use TitleCase for classes
#  lower_case_words for everything else
print(object)

class Dog:   # inherits from 'object'

    def bark(self):
        print("Woof! Woof!")

print(Dog)

dog1 = Dog()
print(dog1)

dog1.bark()







