def keys_with_value(dictionary, value):
    result = []
    for k, v in dictionary.items():
        if value == v:
            result.append(k)
    return result