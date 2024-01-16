#!/usr/bin/env python
# coding: utf-8

from ast import literal_eval

try:
    from participantSolution import *
except ModuleNotFoundError:
    from solutions.main import *


def read_list_of_ints():
    return list(map(int, input()[1:-1].split(", ")))


def read_list_of_strs():
    return [x[1:-1] for x in input()[1:-1].split(", ")]


def read_list_of_strange_things(s: str = None):
    if s is None:
        input_string = input()
    else:
        input_string = s
    if is_it_list(input_string):
        list_of_strings = input_string[1:-1].split(", ")
        result = []
        for item in list_of_strings:
            try:
                result.append(literal_eval(item))
            except:
                result.append(item)
    elif s[:5] == "range":
        result = eval(s)
    return result


def is_it_list(s):
    return s[0] == "[" and s[-1] == "]"


def is_it_tuple(s):
    return s[0] == "(" and s[-1] == ")"


def print_set(s):
    print("{", end="")
    for x in sorted(s):
        if type(x) == str:
            print(f"'{x}'", end=", ")
        else:
            print(x, end=", ")
    print("}")


def print_dict(d):
    print("{", end="")
    for k, v in sorted(d.items()):
        print(f"'{k}': {v}", end=", ")
    print("}")


if __name__ == "__main__":
    x = read_list_of_strange_things()
    # assert callable(multy)
    # x = int(input())
    # print(multy(x))
