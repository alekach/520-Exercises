import math
    total_sum = sum(numbers)
    total_product = math.prod(numbers) if numbers else 1
    return (total_sum, total_product)