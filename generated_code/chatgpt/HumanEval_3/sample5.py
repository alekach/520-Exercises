from typing import List, Iterator
def running_balances(operations: List[int]) -> Iterator[int]:
    balance = 0
    for op in operations:
        balance += op
        yield balance

    return any(balance < 0 for balance in running_balances(operations))