#!/usr/bin/env python
import sys
import shlex
from glob import glob
from subprocess import run, PIPE, CalledProcessError

#  os.popen('cmd')  os.system('cmd')

raw_cmd = """netstat -an"""

raw_cmd_words = shlex.split(raw_cmd)

print("raw_cmd:", raw_cmd)

cmd_words = []

for word in raw_cmd_words:
    expanded = glob(word)
    print("expanded:", expanded)
    if expanded:
        cmd_words.extend(expanded)
    else:
        cmd_words.append(word)


print("cmd_words:", cmd_words)

try:
    proc = run(cmd_words, stdout=PIPE, stderr=PIPE)  # more secure
except CalledProcessError as err:
    print(err)  # log this???
else:
    output = proc.stdout.decode()  # comes in as bytes, decode to str
    lines = output.splitlines()
    for line in lines:
        if "ESTAB" in line:
            print(line)




