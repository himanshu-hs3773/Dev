# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import os
from lib.base import Base
import sys


class Child(Base):

    def new_func(self):
        return self.addition('ab', 'cd')


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    a = 10.0

    print(type(a))
    exit(1)
