    return [
        item
        for i, num in enumerate(numbers)
        for item in ([delimeter] if i > 0 else []) + [num]
    ]