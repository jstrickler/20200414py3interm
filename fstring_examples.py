#!/usr/bin/env python

m = 12.390293
n = 37

print(m)

print("m is %.1f %04d" % (m, n))   # legacy

print("m is {:.1f} {:04d}".format(m, n))  # 2.7 and 3.0 ++

print(f"m is {m:.1f} {n:04d}")   # 3.6 ++

