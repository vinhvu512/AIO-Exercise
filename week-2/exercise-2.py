def count_chars(string):
    res = {}
    for c in string:
        if c not in res.keys():
            res[c] = 1
        else:
            res[c] += 1
    return res
