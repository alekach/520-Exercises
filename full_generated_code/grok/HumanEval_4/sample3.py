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

    n = len(numbers)
    if n == 0:
        raise ValueError("Input list cannot be empty")
    mean = sum(numbers) / n
    total_deviation = 0.0
    for num in numbers:
        total_deviation += abs(num - mean)
    return total_deviation / n