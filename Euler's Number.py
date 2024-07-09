# https://open.kattis.com/problems/eulersnumber

import math

def approximate_e(n):
    approximation = 1
    factorial = 1
    for i in range(1, n + 1):
        factorial *= i
        approximation += 1 / factorial
    return approximation

n = int(input())
print(approximate_e(n))
