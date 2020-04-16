#!/usr/bin/env python

import inspect


class Spam:  # <1>
    pass

#  def FUNCTION(req_pos, ..., *opt_pos, req_named, ..., **opt_name):

def Ham(p1, p2='a', *p3, p4, p5='b', **p6):  # <2>
    print(p1, p2, p3, p4, p5, p6)


for thing in (inspect, Spam, Ham):
    print("{}: Module? {}. Function? {}. Class? {}".format(
        thing.__name__,
        inspect.ismodule(thing),  # <3>
        inspect.isfunction(thing),  # <4>
        inspect.isclass(thing),  # <5>
    ))

print()

print("Function spec for Ham:", inspect.getfullargspec(Ham))  # <6>
print()

print("Current frame:", inspect.getframeinfo(inspect.currentframe()))  # <7>


def myfunction(callback):
    if inspect.isfunction(callback):
        callback()
    else:
        raise TypeError("Arg must be a function")

def hello():
    print("Howdy!!")

myfunction(hello)
# myfunction("Hello")

