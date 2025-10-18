    groups = paren_string.split()
    results = []
    for group in groups:
        stack = []
        max_depth = 0
        for c in group:
            if c == '(':
                stack.append(c)
                max_depth = max(max_depth, len(stack))
            elif c == ')':
                stack.pop()
        results.append(max_depth)
    return results