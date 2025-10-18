    paren_string = paren_string.replace(' ', '')
    result = []
    start = 0
    nesting = 0
    for i, char in enumerate(paren_string):
        if char == '(':
            nesting += 1
        else:
            nesting -= 1
        if nesting == 0:
            result.append(paren_string[start:i + 1])
            start = i + 1
    return result