def rotate(xs, n):
    half1 = xs[:n]
    half2 = xs[n:]
    return half2 + half1