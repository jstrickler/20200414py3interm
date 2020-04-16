#!/usr/bin/env python

# class Dog:
#     def bark(self):
#         print("woof woof")


def woof(self):
    print("Woof! Woof!")


Dog = type('Dog', (), {'bark': woof})


d = Dog()
d.bark()

Cat = type('Cat', (), {'meow': lambda self: print("Meow! Meow!")})

c = Cat()
c.meow()
