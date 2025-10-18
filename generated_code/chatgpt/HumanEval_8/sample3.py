from functools import reduce
import operator
    total_sum = sum(numbers)
    if not numbers:
        total_product = 1
    else:
        total_product = reduce(operator.mul, numbers, 1)
    return (total_sum, total_product)