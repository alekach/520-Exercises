def sum_abs_diff_recursive(numbers, mean, index=0):
    if index == len(numbers):
        return 0
    return abs(numbers[index] - mean) + sum_abs_diff_recursive(numbers, mean, index + 1)

    if not numbers:
        return 0.0
    mean = sum(numbers) / len(numbers)
    total_abs_diff = sum_abs_diff_recursive(numbers, mean)
    return total_abs_diff / len(numbers)