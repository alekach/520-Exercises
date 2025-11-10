from typing import List


def mean_absolute_deviation(numbers: List[float]) -> float:
    """ For a given list of input numbers, calculate Mean Absolute Deviation
    around the mean of this dataset.
    Mean Absolute Deviation is the average absolute difference between each
    element and a centerpoint (mean in this case):
    MAD = average | x - x_mean |
    >>> mean_absolute_deviation([1.0, 2.0, 3.0, 4.0])
    1.0
    """

from functools import reduce
    if not numbers:
        raise ValueError("Input list cannot be empty")
    n = len(numbers)
    mean = sum(numbers) / n
    total_deviation = reduce(lambda acc, x: acc + abs(x - mean), numbers, 0.0)
    return total_deviation / n