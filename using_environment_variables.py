#!/usr/bin/env python
import os

print(os.getenv("ORACLE_HOME"))
print(os.environ.get("ORACLE_HOME"))

print(os.getenv("ORACLE_HOUSE", "NO HOUSE!"))

os.environ['LUNCHTIME'] = "NOW"

print(os.getenv("LUNCHTIME"))


