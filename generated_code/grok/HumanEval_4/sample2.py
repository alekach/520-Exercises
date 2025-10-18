    if not numbers:
        raise ValueError("Input list cannot be empty")
    mean = sum(numbers) / len(numbers)
    deviations = [abs(num - mean) for num in numbers]
    return sum(deviations) / len(numbers)