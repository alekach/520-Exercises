from typing import List


def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    """ Filter an input list of strings only for ones that contain given substring
    >>> filter_by_substring([], 'a')
    []
    >>> filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'a')
    ['abc', 'bacd', 'array']
    """

    if not strings:
        return []    
    first, rest = strings[0], strings[1:]
    if substring in first:
        return [first] + filter_by_substring(rest, substring)
    else:
        return filter_by_substring(rest, substring)