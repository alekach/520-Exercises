    if not numbers:
        return []
    result = [numbers[0]]
    current_max = numbers[0]
    i = 1
    while i < len(numbers):
        current_max = max(current_max, numbers[i])
        result.append(current_max)
        i += 1
    return result