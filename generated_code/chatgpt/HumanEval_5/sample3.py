from itertools import chain
    if not numbers:
        return []    
    pairs = [[num, delimeter] for num in numbers[:-1]]
    return list(chain.from_iterable(pairs)) + [numbers[-1]]