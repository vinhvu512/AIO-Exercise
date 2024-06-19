import math


def factorial(x):
    if x <= 1:
        return 1
    return x * factorial(x - 1)


def approx_sin(x, n):
    res = 0
    for i in range(n):
        res += math.pow(-1, i) * math.pow(x, 2 * i + 1) / factorial(2 * i + 1)
    return res


def approx_cos(x, n):
    res = 0
    for i in range(n):
        res += math.pow(-1, i) * math.pow(x, 2 * i) / factorial(2 * i)
    return res


def approx_sinh(x, n):
    res = 0
    for i in range(n):
        res += math.pow(x, 2 * i + 1) / factorial(2 * i + 1)
    return res


def approx_cosh(x, n):
    res = 0
    for i in range(n):
        res += math.pow(x, 2 * i) / factorial(2 * i)
    return res
