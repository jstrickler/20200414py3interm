#!/usr/bin/env python

def get_message():  #  business logic
    return "Hello"

m = get_message()

print(m)

x = get_message

print(x())
m = x()

def show_message():  # presentation logic   (AKA UI or, even UX)
    m = get_message()
    print(m)

show_message()

def c2f(celsius):
    f = ((9 * celsius) / 5) + 32
    return f

c2f(100)
c2f(37)

