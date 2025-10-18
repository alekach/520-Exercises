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