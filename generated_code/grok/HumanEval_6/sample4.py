    result = []
    for group in paren_string.split():
        depths = []
        current = 0
        for char in group:
            if char == '(':
                current += 1
            elif char == ')':
                current -= 1
            depths.append(current)
        result.append(max(depths) if depths else 0)
    return result