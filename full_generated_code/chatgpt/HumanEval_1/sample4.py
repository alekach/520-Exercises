from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """

    s = paren_string.replace(' ', '')
    if not s:
        return []
    balance = 0
    for i, char in enumerate(s):
        if char == '(':
            balance += 1
        elif char == ')':
            balance -= 1
        if balance == 0:
            group = s[:i+1]
            rest = s[i+1:]
            return [group] + separate_paren_groups(rest)
    return []