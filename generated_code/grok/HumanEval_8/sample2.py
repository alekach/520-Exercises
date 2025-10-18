    from functools import reduce
    from operator import mul
    total_sum = sum(numbers)
    total_product = reduce(mul, numbers, 1) if numbers else 1
    return (total_sum, total_product)