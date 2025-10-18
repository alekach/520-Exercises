    s = paren_string.replace(' ', '')
    result = []
    i = 0
    n = len(s)
    while i < n:
        if s[i] != '(':
            i += 1
            continue
        balance = 0
        for j in range(i, n):
            if s[j] == '(':
                balance += 1
            elif s[j] == ')':
                balance -= 1
            if balance == 0:
                result.append(s[i:j+1])
                i = j + 1
                break
    return result