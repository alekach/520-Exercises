    if len(numbers) < 2:
        return False
    sorted_nums = sorted(numbers)
    for i in range(1, len(sorted_nums)):
        if sorted_nums[i] - sorted_nums[i-1] < threshold:
            return True
    return False