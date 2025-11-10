from typing import List


def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """ Insert a number 'delimeter' between every two consecutive elements of input list `numbers'
    >>> intersperse([], 4)
    []
    >>> intersperse([1, 2, 3], 4)
    [1, 4, 2, 4, 3]
    """

from itertools import chain
    if not numbers:
        return []    
    pairs = [[num, delimeter] for num in numbers[:-1]]
    return list(chain.from_iterable(pairs)) + [numbers[-1]]