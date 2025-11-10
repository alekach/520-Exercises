from typing import List


def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """ Check if in given list of numbers, are any two numbers closer to each other than
    given threshold.
    >>> has_close_elements([1.0, 2.0, 3.0], 0.5)
    False
    >>> has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3)
    True
    """

import bisect
    seen = []
    for num in numbers:
        pos = bisect.bisect_left(seen, num)
        if pos > 0 and abs(num - seen[pos - 1]) < threshold:
            return True
        if pos < len(seen) and abs(seen[pos] - num) < threshold:
            return True
        bisect.insort(seen, num)
    return False