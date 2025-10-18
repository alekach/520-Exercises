from itertools import accumulate
    return min(accumulate(operations), default=0) < 0