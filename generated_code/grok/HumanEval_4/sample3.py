    n = len(numbers)
    if n == 0:
        raise ValueError("Input list cannot be empty")
    mean = sum(numbers) / n
    total_deviation = 0.0
    for num in numbers:
        total_deviation += abs(num - mean)
    return total_deviation / n