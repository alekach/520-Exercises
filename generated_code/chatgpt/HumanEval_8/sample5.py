import math
    nums = [num for num in numbers]
    total_sum = sum(nums)
    total_product = math.prod(nums) if nums else 1
    return (total_sum, total_product)