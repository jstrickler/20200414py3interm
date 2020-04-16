#!/usr/bin/env python
from unittest import TestCase, main
from knight import Knight

class TestKnight(TestCase):

    def test_knight_has_all_attributes(self):
        k = Knight('Arthur', 'King', 'red')
        for attr in 'name', 'title', 'color':
            self.assertTrue(hasattr(k, attr))

    def test_knight_attr_has_correct_value(self):
        args = 'Arthur', 'King', 'red'
        attrs = 'name', 'title', 'color'
        k = Knight(*args)
        for attr, arg in zip(attrs, args):
            self.assertTrue(getattr(k, attr) == arg)




if __name__ == '__main__':
    main()
