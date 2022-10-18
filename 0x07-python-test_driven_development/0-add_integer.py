#!/usr/bin/python3
"""
This is the "0-add_integer" module.
The 0-add_integer module has one function add_integer(a, b)
"""
def add_integer(a, b=98):
""" This function takes in max of two integer args and min of one wher the second can be replaced my 98."""



    if type(a) is float:
        int(a)
    if type(b) is float:
        int(b)
    if type(a) is not int:
        raise TypeError(a must be an integer)
    if type(b) is not int:
        raise TypeError(b must be an integer)
    return (a + b)
