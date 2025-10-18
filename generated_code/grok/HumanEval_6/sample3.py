    result = []
    for group in paren_string.split():
        stack = []
        max_depth = 0
        for char in group:
            if char == '(':
                stack.append(char)
                max_depth = max(max_depth, len(stack))
            elif char == ')':
                if stack:
                    stack.pop()
        result.append(max_depth)
    return result