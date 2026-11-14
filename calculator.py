# https://github.com/ahoyos30/lab11-AH-VS/blob/main/test_calculator.py
# Partner 1: Andres Hoyos
# Parnter 2: Varit Seeherunvong

"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""

import math

def square_root(a):
    return math.sqrt(a)
def hypotenuse(a, b):
    return math.hypot(a, b)
def add(a, b): 
    return a + b
def subtract(a, b):
    return a - b
def mul(a, b):
    return a * b
def div(a, b):
    if a == 0:
        raise ZeroDivisionError
    return b / a
def exp(a, b):
    return a ** b
def logarithm(a, b):
    return math.log(b, a)