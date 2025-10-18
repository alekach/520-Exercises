    sorted_nums = sorted(numbers)
    return any(b - a < threshold for a, b in zip(sorted_nums, sorted_nums[1:]))