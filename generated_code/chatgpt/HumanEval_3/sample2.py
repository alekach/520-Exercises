from itertools import accumulate
    return any(balance < 0 for balance in accumulate(operations))