    paren_string = paren_string.replace(' ', '')
    groups = []
    balance = 0
    start = 0
    for i, char in enumerate(paren_string):
        if char == '(':
            balance += 1
        elif char == ')':
            balance -= 1
        if balance == 0:
            groups.append(paren_string[start:i+1])
            start = i + 1
    return groups