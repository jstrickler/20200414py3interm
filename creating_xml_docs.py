#!/usr/bin/env python
import lxml.etree as ET

people = [
    (1, 'Melinda', 'Gates', 'Gates Foundation', '1964-08-15'),
    (23, 'Steve', 'Jobs', 'Apple', '1955-02-24'),
    (42, 'Larry', 'Wall', 'Perl', '1954-09-27'),
    (37, 'Paul', 'Allen', 'Microsoft', '1953-01-21'),
    (28, 'Larry', 'Ellison', 'Oracle', '1944-08-17'),
    (43, 'Bill', 'Gates', 'Microsoft', '1955-10-28'),
    (97, 'Mark', 'Zuckerberg', 'Facebook', '1984-05-14'),
    (31, 'Sergey','Brin', 'Google', '1973-08-21'),
    (29, 'Larry', 'Page', 'Google', '1973-03-26'),
    (18, 'Linus', 'Torvalds', 'Linux', '1969-12-28'),
]

root = ET.Element('persons')

for rec_id, first_name, last_name, product, dob in people:
    p = ET.SubElement(root, 'person', record_id=str(rec_id))
    fn = ET.SubElement(p, "first_name")
    fn.text = first_name
    ET.SubElement(p, 'last_name').text = last_name
    ET.SubElement(p, 'first_name').text = first_name
    ET.SubElement(p, 'product').text = product
    ET.SubElement(p, 'date_of_birth').text = dob


print(ET.tostring(root, pretty_print=True, xml_declaration=True).decode())

doc = ET.ElementTree(root)

doc.write('computer_people.xml', pretty_print=True, xml_declaration=True)

