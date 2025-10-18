    s = paren_string.replace(' ', '')
    if not s:
        return []
    balance = 0
    for i, char in enumerate(s):
        if char == '(':
            balance += 1
        elif char == ')':
            balance -= 1
        if balance == 0:
            group = s[:i+1]
            rest = s[i+1:]
            return [group] + separate_paren_groups(rest)
    return []