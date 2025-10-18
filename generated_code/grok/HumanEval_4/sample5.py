from functools import reduce
    if not numbers:
        raise ValueError("Input list cannot be empty")
    n = len(numbers)
    mean = sum(numbers) / n
    total_deviation = reduce(lambda acc, x: acc + abs(x - mean), numbers, 0.0)
    return total_deviation / n