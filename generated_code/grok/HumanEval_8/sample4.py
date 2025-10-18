from functools import reduce
from operator import add, mul
    return reduce(add, numbers, 0), reduce(mul, numbers, 1)