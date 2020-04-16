#!/usr/bin/env python

if True:
    x = 100  # (file) GLOBAL name

print(x)   # BUILTIN name

def spam():
    y = 42   # LOCAL name to spam()   NONLOCAL name to ham()
    x = "wombat"
    print(y * 10)
    print(x * 10)

    def ham():
        y = 888  # local name to ham()
        return y

    return ham

f = spam()
print("f is", f)
result = f()
print(result)
print("x is", x)

#  local -> nonlocal (nested) -> global -> builtin
