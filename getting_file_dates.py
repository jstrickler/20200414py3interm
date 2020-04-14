#!/usr/bin/env python
import os
from datetime import datetime

for file_name in os.listdir():
    if file_name.endswith('.py'):
        raw_file_timestamp = os.path.getmtime(file_name)
        file_timestamp = datetime.fromtimestamp(raw_file_timestamp)
        print(file_timestamp.date(), file_name)
