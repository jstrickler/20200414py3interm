#!/usr/bin/env python

#            pos          named
#         req     opt   req   opt
def wacky(p1, p2, *p3, p4, p5, **p6):
    print("p1: {}".format(p1))
    print("p2: {}".format(p2))
    print("p3: {}".format(p3))
    print("p4: {}".format(p4))
    print("p5: {}".format(p5))
    print("p6: {}".format(p6))
    print("=" * 10, '\n')

wacky('alpha', 'beta', p4="gamma", p5="delta")

wacky('alpha', 'beta', "a", "b", "c", p5="delta", p4="gamma")

wacky('alpha', 'beta', "a", "b", "c", p5="delta", p4="gamma", country="Rwanda", liquor="Scotch")


def ham(a, b):
    print(a, b)

ham(1, 2)
ham(b=2, a=1)


def wacky(*, p1, p2, p4, p5):
    print("p1: {}".format(p1))
    print("p2: {}".format(p2))
    print("p4: {}".format(p4))
    print("p5: {}".format(p5))
    print("=" * 10, '\n')

def fd1(file_name, *, year, month, day):
    pass

#                  named -- order doesn't matter
fd1("wombats.txt", month=8, day=1, year=2020)

#                  positional -- order matters UNLESS name is specified
def fd2(file_name, year, month, day):
    pass

fd2("quokkas.txt", 2020, 8, 1)
fd2("quokkas.txt", month=8, day=1, year=2020)  # specifying POSITIONAL by name


def fd3(file_name, *, year=None, month=None, day=None):
    pass

fd3("rutabagas.txt")
fd3("rutabagas.txt", year=2020)
fd3("rutabagas.txt", year=2020, day=1)

def generic(*args, **kwargs):
    print(args, kwargs)








