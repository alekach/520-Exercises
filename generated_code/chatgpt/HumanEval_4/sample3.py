    n = len(numbers)
    if n == 0:
        return 0.0
    total = 0.0
    for num in numbers:
        total += num
    mean = total / n
    abs_diff_sum = 0.0
    for num in numbers:
        abs_diff_sum += abs(num - mean)
    mad = abs_diff_sum / n
    return mad