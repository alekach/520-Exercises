    def max_depth(group: str) -> int:
        current = 0
        maximum = 0
        for char in group:
            if char == '(':
                current += 1
                maximum = max(maximum, current)
            elif char == ')':
                current -= 1
        return maximum
    return [max_depth(group) for group in paren_string.split()]