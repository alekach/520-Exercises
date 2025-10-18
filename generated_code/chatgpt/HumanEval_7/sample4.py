    if not strings:
        return []    
    first, rest = strings[0], strings[1:]
    if substring in first:
        return [first] + filter_by_substring(rest, substring)
    else:
        return filter_by_substring(rest, substring)