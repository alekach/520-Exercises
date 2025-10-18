    if not numbers:
        return []    
    current_max = numbers[0]
    result = [current_max]    
    for num in numbers[1:]:
        if num > current_max:
            current_max = num
        result.append(current_max)
    return result