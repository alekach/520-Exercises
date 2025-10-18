    if not numbers:
        return numbers    
    for i in range(1, len(numbers)):
        numbers[i] = max(numbers[i], numbers[i - 1])
    return numbers