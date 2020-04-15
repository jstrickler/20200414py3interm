#!/usr/bin/env python


def spam(a, b, c):
    print("a:", a)
    print("b:", b)
    print("c:", c)
    print()

spam(1, 2, 3)
spam('alpha', 'beta', 'gamma')

spam([1], [1,2,3], (4, 5))

data = ['President', 'Richard', 'Milhous']


spam(data[0], data[1], data[2])

spam(*data)

def ham(**kwargs):
    print(kwargs)


data = {
    'file_name': "koalas.txt",
    'age': 98,
#    'country': 'Lithuania',
}

ham(file_name="wombats.txt", age=34, country="Burkina Faso")
ham(**data)
ham()


