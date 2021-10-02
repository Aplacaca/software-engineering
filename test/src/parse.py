import re
import sys
from typing import Union

Users, Maps, Funds, Credits, Gifts, Bombs, Barriers, Userlocs = [], [], [], [], [], [], [], []


class User(object):
    def __init__(self, name: str, loc: int = 0):
        self.name = name
        self.loc = loc

    def __str__(self):
        return "[User]: {}'s loc is {}".format(self.name, self.loc)


class Map(object):
    def __init__(self, user: User, loc: int, level: int, length: int = 70):
        self.user = user
        self.loc = loc
        self.level = level


class Fund(object):
    def __init__(self, user: Union[User, str], number: int):
        self.user = user
        self.number = number


class Credit(object):
    def __init__(self, user: User, number: int):
        self.user = user
        self.number = number


class Gift(object):
    def __init__(self, user: User, tool: str, n: int):
        self.user = user
        self.tool = tool
        self.n = n


class Bomb(object):
    def __init__(self, n: int = 0, user: User='name'):
        self.user = user
        self.n = n


class Barrier(object):
    def __init__(self, n: int, user: User='name'):
        self.user = user
        self.n = n


class Userloc(object):
    def __init__(self, user: User, n: int, m: int=0):
        self.user = User
        self.n = n
        self.m = m


def parser(file: str):

    with open(file, 'r') as f:
        for line in f.readlines():
            split = line.split(' ')
            if split[0] == 'preset':
                cls_name = split[1].capitalize()
                getattr(sys.modules[__name__], cls_name+'s').append(getattr(sys.modules[__name__], cls_name)(*split[2:]))
            else:
                ...


def main():
    # parser('/Users/gpl/repos/SoftwareEngineer/test/testcase/input/inputcase_1.txt')
    # print(len(Users))
    user = User('hello',10)
    print(user)


if __name__ == '__main__':
    main()