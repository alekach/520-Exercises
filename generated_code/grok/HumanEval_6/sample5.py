from itertools import accumulate
    def get_max_depth(group: str) -> int:
        deltas = (1 if c == '(' else -1 for c in group)
        depths = accumulate(deltas, initial=0)
        return max(depths)
    groups = paren_string.split()
    return [get_max_depth(group) for group in groups if group]