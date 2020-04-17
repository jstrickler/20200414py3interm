#!/usr/bin/env python
import lxml.etree as ET

doc = ET.parse('computer_people.xml')

root = doc.getroot()

print(root)
print(root.tag)

for person in root.findall('person'):
    id_num = person.get('record_id', -1)
    first_name = person.findtext('first_name')
    last_name = person.findtext('last_name')
    print(id_num, first_name, last_name)

print('-' * 60)

doc = ET.parse('DATA/solar.xml')

#  doc.findall()  same as doc.getroot().findall()
for planet in doc.findall('.//planet'):  # XPath
    print(planet.get('planetname'))
    for moon in planet.findall('moon'):
        print(f"\t{moon.text}")





