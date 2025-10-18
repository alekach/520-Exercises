    if not numbers:
        return []
    return [x for num in numbers for x in (num, delimeter)][:-1]