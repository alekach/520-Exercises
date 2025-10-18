    paren_string = paren_string.replace(' ', '')
    result = []
    start = 0
    stack = []
    for i, char in enumerate(paren_string):
        if char == '(':
            stack.append(i)
        else:
            if stack:
                stack.pop()
            if not stack:
                result.append(paren_string[start:i + 1])
                start = i + 1
    return result