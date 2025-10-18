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