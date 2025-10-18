import itertools
    for a, b in itertools.combinations(numbers, 2):
        if abs(a - b) < threshold:
            return True
    return False