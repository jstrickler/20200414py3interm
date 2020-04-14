#!/usr/bin/env python
import os

files = os.listdir('DATA')
print(files, '\n')

files = os.listdir('.')
print(files, '\n')

for node in os.scandir('DATA'):
    print(node.name, node.is_dir(), node.is_file(), node.stat())
    print(bin(node.stat().st_mode))
    print()

SKIP_LIST = ['.git', 'TEMP']

for curr_dir, dir_list, file_list in os.walk('.'):
    for skip_dir in SKIP_LIST:
        if skip_dir in dir_list:
            dir_list.remove(skip_dir)
    for file_name in file_list:
        if file_name.endswith('.py'):
            file_path = os.path.join(curr_dir, file_name) # path + '/' + name
            file_size = os.path.getsize(file_path)
            if file_size > 4000:
                print(file_path)

