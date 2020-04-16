#!/usr/bin/env python
from president import President

p = President(26)

print(p)

print(p.first_name, p.last_name)

field_name = "birth_place"

field_value = getattr(p, field_name, "NO SUCH ATTRIBUTE, DUDE!")
print(field_value, '\n')

for attr in "first_name", "birth_state", "favorite_color", "party", "gender":
    print(attr, hasattr(p, attr))
print()

def print_stuff(obj):
    if hasattr(obj, "print"):
        obj.print()
    else:
        print(f"sorry, {obj} cannot print")

print_stuff(p)

print(p.party)

delattr(President, "party")

try:
    print(p.party)
except:
    print("No party!")

setattr(p, "color", "purple")

print(p.color)
