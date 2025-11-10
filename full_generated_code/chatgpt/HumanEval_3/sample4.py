from typing import List


def below_zero(operations: List[int]) -> bool:
    """ You're given a list of deposit and withdrawal operations on a bank account that starts with
    zero balance. Your task is to detect if at any point the balance of account fallls below zero, and
    at that point function should return True. Otherwise it should return False.
    >>> below_zero([1, 2, 3])
    False
    >>> below_zero([1, 2, -4, 5])
    True
    """

    def step(balance, op):
        new_balance = balance + op
        if new_balance < 0:
            raise ValueError("Below zero")
        return new_balance

    from functools import reduce

    try:
        reduce(step, operations, 0)
        return False
    except ValueError:
        return True