from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """

from typing import List, Generator

def _paren_groups_generator(s: str) -> Generator[str, None, None]:
    start = 0
    balance = 0

    for i, char in enumerate(s):
        if char == '(':
            if balance == 0:
                start = i
            balance += 1
        elif char == ')':
            balance -= 1

        if balance == 0 and char == ')':
            yield s[start:i+1]

    cleaned = paren_string.replace(' ', '')
    return list(_paren_groups_generator(cleaned))