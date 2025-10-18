    if not numbers:
        return []
    result = []
    for num in numbers[:-1]:
        result += [num, delimeter]
    result += [numbers[-1]]
    return result