#!/usr/bin/env python

NUMBERS = [800,80,1000,32,255,400,5,5000]

def spam():
    print("Hello from spam()")

def ham():
    print("Hello from ham()")

def _toast():  # pseudo-private  AKA privacy by agreement
    print("hello from _toast()")

# print("My name is", __name__)

if __name__ == '__main__':
    ham()
    ham()
    spam()
    print("Hi, Mom!!")

