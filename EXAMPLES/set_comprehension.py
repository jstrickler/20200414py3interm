#!/usr/bin/env python

import re

with open("../DATA/mary.txt") as mary_in:
    contents = mary_in.read()

s = {w.lower() for w in re.split(r'\W+', contents) if w} #<1>
print(s)

