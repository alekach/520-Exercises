    groups = paren_string.split()    
    def max_depth(group: str) -> int:
        depth = 0
        max_d = 0
        for c in group:
            if c == '(':
                depth += 1
                max_d = max(max_d, depth)
            elif c == ')':
                depth -= 1
        return max_d    
    return [max_depth(group) for group in groups]