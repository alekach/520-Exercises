    count = len(numbers)
    if count == 0:
        return 0.0
    total = sum(numbers)
    mean = total / count
    abs_differences = map(lambda x: abs(x - mean), numbers)
    total_abs_diff = sum(abs_differences)
    mad = total_abs_diff / count
    return mad