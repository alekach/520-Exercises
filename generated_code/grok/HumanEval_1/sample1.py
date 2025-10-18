    result = []
    current = ""
    nesting = 0
    for char in paren_string:
        if char == ' ':
            continue
        current += char
        if char == '(':
            nesting += 1
        elif char == ')':
            nesting -= 1
            if nesting == 0:
                result.append(current)
                current = ""
    return result