from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """

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