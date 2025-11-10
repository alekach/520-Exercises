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

def sum_abs_diff_recursive(numbers, mean, index=0):
    if index == len(numbers):
        return 0
    return abs(numbers[index] - mean) + sum_abs_diff_recursive(numbers, mean, index + 1)

    if not numbers:
        return 0.0
    mean = sum(numbers) / len(numbers)
    total_abs_diff = sum_abs_diff_recursive(numbers, mean)
    return total_abs_diff / len(numbers)