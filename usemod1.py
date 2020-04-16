#!/usr/bin/env python
import sys
# from pkg.pkg import module
from jeffco.flotsam import banana
import pastable

banana.spam()
banana.ham()

print(pastable.nums)

# naughty naughty programmer:
# banana._toast()
print(banana.NUMBERS, '\n')

for path in sys.path:
    print(path)
print('-' * 60)
# sys.path = "." + PYTHONPATH + sys.prefix/lib

print(sys.prefix)
print(sys.executable)



