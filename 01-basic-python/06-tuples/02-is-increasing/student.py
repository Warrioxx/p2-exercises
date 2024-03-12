def is_increasing(ns):
    ms = ns[1:]
    pairs = zip(ns, ms)

    for (x, y) in pairs:
        if x > y:
            return False
    return True