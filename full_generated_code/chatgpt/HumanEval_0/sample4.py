from typing import List


def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """ Check if in given list of numbers, are any two numbers closer to each other than
    given threshold.
    >>> has_close_elements([1.0, 2.0, 3.0], 0.5)
    False
    >>> has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3)
    True
    """

    if threshold <= 0:
        return False
    bucket_map = {}
    bucket_size = threshold
    for num in numbers:
        bucket = int(num // bucket_size)
        if bucket in bucket_map:
            return True
        if (bucket - 1 in bucket_map and abs(num - bucket_map[bucket - 1]) < threshold):
            return True
        if (bucket + 1 in bucket_map and abs(num - bucket_map[bucket + 1]) < threshold):
            return True
        bucket_map[bucket] = num
    return False