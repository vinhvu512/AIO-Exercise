def md_nre_single_sample(y, y_hat, n, p):
    result = (y ** (1/n) - y_hat ** (1/n)) ** p
    return result