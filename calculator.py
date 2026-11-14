"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""

import math

def square_root(a): math.sqrt(a)
def hypotenuse(a, b): math.hypot(a, b)
def add(a, b): 
    return a + b
def sub(a, b):
    return a - b
def mul(a, b):
    return a * b
def div(a, b):
    if a == 0:
        raise ZeroDivisionError
    return b / a
def exp(a, b):
    return a ** b
def logarithm(a, b): math.log(b, a)