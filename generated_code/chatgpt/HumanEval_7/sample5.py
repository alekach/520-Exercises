from functools import reduce
    return reduce(
        lambda acc, s: acc + [s] if substring in s else acc,
        strings,
        []
    )