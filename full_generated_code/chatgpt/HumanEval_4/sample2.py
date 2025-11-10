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

    count = len(numbers)
    if count == 0:
        return 0.0
    total = sum(numbers)
    mean = total / count
    abs_differences = map(lambda x: abs(x - mean), numbers)
    total_abs_diff = sum(abs_differences)
    mad = total_abs_diff / count
    return mad