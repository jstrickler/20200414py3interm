#!/usr/bin/env python
from abc import ABCMeta, abstractmethod

class CardDeckBase(metaclass=ABCMeta):


    def wombat(self):
        print("I am a wombat")

    @abstractmethod
    def draw(self):
        pass

    @abstractmethod
    def shuffle(self):
        pass

    # @abstractmethod
    # def spam(self):
    #     pass

    @property
    @abstractmethod
    def dealer(self):
        pass

    @dealer.setter
    @abstractmethod
    def dealer(self, value):
        pass

