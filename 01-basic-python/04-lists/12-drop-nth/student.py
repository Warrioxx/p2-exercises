def drop_nth(xs, n):
    half1 = xs[:n]
    half2 = xs[n+1:]
    return half1 + half2