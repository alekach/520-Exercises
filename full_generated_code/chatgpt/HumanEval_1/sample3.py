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
    result = []
    i = 0
    n = len(s)
    while i < n:
        if s[i] != '(':
            i += 1
            continue
        balance = 0
        for j in range(i, n):
            if s[j] == '(':
                balance += 1
            elif s[j] == ')':
                balance -= 1
            if balance == 0:
                result.append(s[i:j+1])
                i = j + 1
                break
    return result