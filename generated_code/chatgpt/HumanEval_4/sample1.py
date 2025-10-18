    if not numbers:
        return 0.0
    mean = sum(numbers) / len(numbers)
    absolute_differences = [abs(x - mean) for x in numbers]
    mad = sum(absolute_differences) / len(numbers)
    return mad