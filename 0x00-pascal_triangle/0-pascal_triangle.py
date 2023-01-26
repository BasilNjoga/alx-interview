#!/usr/bin/python3
"""
This is a function to return a pascals triangle
"""


def factorial(n):
    if n < 2:
        return 1
    else:
        return n * factorial(n-1)


def pascal_triangle(n):
    mylist = [[]]
    if n <= 0:
        return mylist
    mylist = []
    for j in range(n):
        new = []
        for i in range(j+1):
            value = factorial(j)/(factorial(i) * factorial(j-i))
            new.append(int(value))
        mylist.append(new)
    return mylist
