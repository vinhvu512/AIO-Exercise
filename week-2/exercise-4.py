import numpy as np


def levenshtein_distance(token1, token2):
    num_rows = len(token1) + 1
    num_cols = len(token2) + 1
    D = np.zeros((num_rows, num_cols))
    for i in range(num_rows):
        D[i, 0] = i
    for i in range(num_cols):
        D[0, i] = i
    for i in range(1, num_rows):
        for j in range(1, num_cols):
            D[i, j] = min(
                D[i - 1, j] + 1,
                D[i, j - 1] + 1,
                D[i - 1, j - 1] + 1 if token1[i - 1] != token2[j - 1] else D[i - 1, j - 1]
            )
    return D[-1, -1]
