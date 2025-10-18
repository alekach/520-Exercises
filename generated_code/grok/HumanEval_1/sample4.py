    def helper(i: int) -> List[str]:
        if i >= len(paren_string):
            return []
        while i < len(paren_string) and paren_string[i] == ' ':
            i += 1
        if i >= len(paren_string):
            return []
        start = i
        nesting = 0
        while i < len(paren_string):
            if paren_string[i] == ' ':
                i += 1
                continue
            if paren_string[i] == '(':
                nesting += 1
            elif paren_string[i] == ')':
                nesting -= 1
            i += 1
            if nesting == 0:
                break
        group = ''.join(c for c in paren_string[start:i] if c != ' ')
        return [group] + helper(i)
    return helper(0)