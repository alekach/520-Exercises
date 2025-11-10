from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """

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