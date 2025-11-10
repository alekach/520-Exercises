from typing import List


def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """ Insert a number 'delimeter' between every two consecutive elements of input list `numbers'
    >>> intersperse([], 4)
    []
    >>> intersperse([1, 2, 3], 4)
    [1, 4, 2, 4, 3]
    """

from functools import reduce
    if not numbers:
        return []    
    def reducer(acc: List[int], curr: int) -> List[int]:
        if not acc:
            return [curr]
        return acc + [delimeter, curr]    
    return reduce(reducer, numbers, [])