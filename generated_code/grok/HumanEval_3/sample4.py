    balance = 0
    for i in range(len(operations)):
        balance += sum(operations[:i+1])
        if balance < 0:
            return True
    return False