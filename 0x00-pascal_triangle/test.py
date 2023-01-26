#!/usr/bin/python3

def factorial(n):
    sum = 1
    if n < 2:
        return 1
    else:
        return n * factorial(n-1)
    return sum

print(factorial(3))