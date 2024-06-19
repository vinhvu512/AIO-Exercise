import math


def is_number(x):
    try:
        float(x)
    except ValueError:
        return False
    return True


def activation_function():
    x = input("Input x = ")
    if not is_number(x):
        print("x must be a number")
        return
    x = float(x)
    typ = input("Input activation Function (sigmoid | relu | elu): ")
    res = None
    if typ == "relu":
        res = x if x >= 0 else 0
    elif typ == "sigmoid":
        res = 1 / (1 + math.exp(-x))
    elif typ == "elu":
        alpha = 0.01
        res = x if x > 0 else alpha * (math.exp(x) - 1)
    else:
        print(f"{typ} is not supported")
        return
    print(f"{typ}: f({x}) = {res}")
