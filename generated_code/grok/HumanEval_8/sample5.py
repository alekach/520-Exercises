from functools import reduce
    return reduce(lambda acc, x: (acc[0] + x, acc[1] * x), numbers, (0, 1))