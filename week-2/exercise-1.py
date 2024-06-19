def find_top_max(lst, k):
    res = []
    for i in range(len(lst) - k + 1):
        res.append(max(lst[i:i + k]))
    return res


find_top_max(lst=[3, 4, 5, 1, -44, 5, 10, 12, 33, 1], k=3)
