import re
    groups = paren_string.split()
    def max_depth_regex(group: str) -> int:
        depth = 0
        s = group
        while True:
            new_s = re.sub(r'\(\)', '', s)
            if new_s == s:
                break
            s = new_s
            depth += 1
        return depth
    return [max_depth_regex(group) for group in groups]