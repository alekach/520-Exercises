    balance = 0
    for i, op in enumerate(operations):
        balance += op
        if balance < 0:
            return True
    return False