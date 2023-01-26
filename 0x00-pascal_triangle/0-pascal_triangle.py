#!/usr/bin/python3
"""
This is a function to return a pascals triangle
"""
from math import factorial


def pascal_triangle(n):
    mylist = []
    if n <= 0:
        return mylist
    for j in range(n):
        new = []
        for i in range(j+1):
            value = factorial(j)/(factorial(i) * factorial(j-i))
            new.append(int(value))
        mylist.append(new)
    return mylist
