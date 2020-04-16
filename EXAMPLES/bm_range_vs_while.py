#!/usr/bin/env python

import timeit


test_code_one = '''
values = []
for i in range(10000):
    values.append(i)
'''  # <2>

test_code_two = '''
values = []
i = 0
while i < 10000:
    values.append(i)
    i += 1
'''  # <2>

t1 = timeit.Timer(test_code_one)  # <3>
t2 = timeit.Timer(test_code_two)  # <3>

REPEAT_COUNT = 10000

print("test one:")
print(t1.timeit(REPEAT_COUNT))  # <4>
print()

print("test two:")
print(t2.timeit(REPEAT_COUNT))  # <4>
print()
