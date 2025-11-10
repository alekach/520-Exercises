from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """

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