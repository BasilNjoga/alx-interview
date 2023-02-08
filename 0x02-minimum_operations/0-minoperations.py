#!/usr/bin/python3
"""
takes a single character copying and pasting to 
get the number of steps
"""


def minOperations(n):
    count = 0
    for i in range(n):
        count += 1
        for j in range(count):
            print("H", end = '')
        print("\n", end = '')

