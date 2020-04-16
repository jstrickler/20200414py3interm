#!/usr/bin/env python
from functools import wraps
from datetime import datetime

def times_three(original_function):

    @wraps(original_function)
    def replacement_function(*args, **kwargs):
        result = original_function(*args, **kwargs)
        return 3 * result

    return replacement_function

def times_five(original_function):

    @wraps(original_function)
    def replacement_function(*args, **kwargs):
        result = original_function(*args, **kwargs)
        return 5 * result

    return replacement_function



def time_stamp(original_function):

    @wraps(original_function)
    def replacement_function(*args, **kwargs):
        print(datetime.now())
        result = original_function(*args, **kwargs)
        return 10 * result

    return replacement_function

@time_stamp
def spam():
    print("Hello from spam!")
    return 10
# spam = wrapper(spam)

@time_stamp
def ham():
    print("ham ham ham")
    return "abc"

print(spam())
print(ham())

print(spam.__name__)
print(ham.__name__)


@times_three
def a():
    return 10

@times_five
def b():
    return 10


@times_five
@times_three
def c():
    return 10

@times_three
@times_three
def d():
    return 10



print("a(): {}\n".format(a()))
print("b(): {}\n".format(b()))
print("c(): {}\n".format(c()))
print("d(): {}\n".format(d()))
