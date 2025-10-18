    paren_string = paren_string.replace(' ', '')
    stack = []
    current_group = []
    groups = []
    for char in paren_string:
        current_group.append(char)
        if char == '(':
            stack.append(char)
        elif char == ')':
            if stack:
                stack.pop()
        if not stack and current_group:
            groups.append(''.join(current_group))
            current_group = []
    return groups