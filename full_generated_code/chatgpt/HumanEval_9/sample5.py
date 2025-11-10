from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """

    def helper(index: int, current_max: int) -> List[int]:
        if index == len(numbers):
            return []
        new_max = max(numbers[index], current_max)
        return [new_max] + helper(index + 1, new_max)    
    return helper(0, float('-inf'))