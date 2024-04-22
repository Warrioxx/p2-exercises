import re

def only_digits(string):
    return re.fullmatch("[1234567890]*", string)