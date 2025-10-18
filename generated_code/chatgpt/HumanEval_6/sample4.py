        def max_depth_recursive(s: str, start=0) -> int:
        max_d = 0
        i = start
        while i < len(s):
            if s[i] == '(':
                j = i + 1
                open_count = 1
                while j < len(s) and open_count > 0:
                    if s[j] == '(':
                        open_count += 1
                    elif s[j] == ')':
                        open_count -= 1
                    j += 1
                inner_depth = max_depth_recursive(s, i + 1)
                max_d = max(max_d, 1 + inner_depth)
                i = j
            else:
                i += 1
        return max_d
    groups = paren_string.split()
    return [max_depth_recursive(group) for group in groups]