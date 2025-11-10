from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """

    paren_string = paren_string.replace(' ', '')
    stack = []
    current_group = []
    groups = []
    for char in paren_string:
        current_group.append(char)
        if char == '(':
            stack.append(char)
        elif char == ')':
            if stack:
                stack.pop()
        if not stack and current_group:
            groups.append(''.join(current_group))
            current_group = []
    return groups