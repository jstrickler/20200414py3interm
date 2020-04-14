#!/usr/bin/env python

# for VAR, ... in ITERABLE:
#    use VAR....

fruits = ["pomegranate", "cherry", "apricot", "apple",
"lemon", "kiwi", "orange", "lime", "watermelon", "guava",
"papaya", "fig", "pear", "banana", "tamarind", "persimmon",
"elderberry", "peach", "blueberry", "lychee", "grape", "date" ]

for fruit in fruits:
    print(fruit.upper())
print()

target = 'x'

for fruit in fruits:
    if fruit.startswith(target):
        print(fruit)
        break
else:
    print("NOT FOUND")


while True:
    name = input("Enter name: ")
    if name == 'q':
        break
    if name == '':
        continue
    print("Welcome,", name)




