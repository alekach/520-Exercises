    paren_string = paren_string.replace(' ', '')
    result = []
    current = []
    nesting = 0
    for char in paren_string:
        current.append(char)
        if char == '(':
            nesting += 1
        else:
            nesting -= 1
            if nesting == 0:
                result.append(''.join(current))
                current = []
    return result