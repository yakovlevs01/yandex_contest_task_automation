#!/usr/bin/env python
# coding: utf-8

from ast import literal_eval
from typing import Any

try:
    try:
        from participantSolution import *
    except ModuleNotFoundError:
        from solutions.main import *
except:
    pass


def read_dict_str_int():
    s = input()
    if s == "{}":
        return {}
    return literal_eval(s)


def read_enumeration_of_ints():
    s = input()
    if s == "":
        return []
    return list(map(int, s.split(", ")))


def read_enumeration_of_strs():
    s = input()
    if s == "":
        return []
    return s.split(", ")


def read_enumeration_of_strange_things():
    s = input()
    if s == "":
        return []
    result = []
    for item in s.split(", "):
        try:
            result.append(literal_eval(item))
        except:
            result.append(item)
    return result


def read_list_of_ints() -> tuple[set[Any], int]:
    s = input()
    if s == "[]":
        return []
    return list(map(int, s[1:-1].split(", ")))


def read_list_of_strs():
    s = input()

    if s == "[]":
        return []
    return [x[1:-1] for x in s[1:-1].split(", ")]


def read_list_of_any_or_str_or_range_or_tuple(s: str = None):
    input_string = input() if s is None else s
    if input_string == "[]":
        return []
    if input_string == "()":
        return tuple()
    if input_string in ("''", '""'):
        return str()
    if input_string[:6] == "range(" and input_string[-1] == ")":
        return eval(input_string)
    if is_it_list(input_string):
        list_of_strings = input_string[1:-1].split(", ")
        result = []
        for item in list_of_strings:
            try:
                result.append(literal_eval(item))
            except:
                result.append(item)
        return result
    return input_string


def read_list_of_strange_things(s: str = None):
    input_string = input() if s is None else s
    if input_string == "[]":
        return []
    if is_it_list(input_string):
        list_of_strings = input_string[1:-1].split(", ")
        result = []
        for item in list_of_strings:
            try:
                result.append(literal_eval(item))
            except:
                result.append(item)
    return result


def is_it_list(s):
    return s[0] == "[" and s[-1] == "]"


def is_it_tuple(s):
    return s[0] == "(" and s[-1] == ")"


def all_items_are_the_same_type(x):
    if not x:
        return True

    first_type = type(next(iter(x)))
    return all(isinstance(item, first_type) for item in x)


def set_to_str_for_print(s):
    if len(s) == 0:
        return "set()"
    if all_items_are_the_same_type(s):
        if isinstance(next(iter(s)), str):
            result = "{" + ", ".join([f"'{x}'" for x in sorted(s)]) + "}"
        else:
            result = "{" + ", ".join(map(str, sorted(s))) + "}"
    else:
        result = (
            "{"
            + ", ".join(sorted([f"'{x}'" * isinstance(x, str) + str(x) * (not isinstance(x, str)) for x in s]))
            + "}"
        )

    return result


def dict_to_str_for_print(d):
    result = "{"
    for k, v in sorted(d.items()):
        result += f"'{k}': {v}" + ", "
    result = result[:-2]
    result += "}"
    return result


if __name__ == "__main__":
    d = literal_eval(input())
    print(bin_ip(d))
