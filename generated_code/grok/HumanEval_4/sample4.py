    if not numbers:
        raise ValueError("Input list cannot be empty")
    n = len(numbers)
    mean = sum(numbers) / n
    return sum(map(lambda x: abs(x - mean), numbers)) / n