from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """

from itertools import accumulate
    def get_max_depth(group: str) -> int:
        deltas = (1 if c == '(' else -1 for c in group)
        depths = accumulate(deltas, initial=0)
        return max(depths)
    groups = paren_string.split()
    return [get_max_depth(group) for group in groups if group]