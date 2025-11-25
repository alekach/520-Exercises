from typing import List

# Assumption: the input list is non-empty (as MAD around the mean is undefined for empty lists)
numbers: List[float]
result = mean_absolute_deviation(numbers)   # this is the value returned by the function

# Specification 1: Non-negativity
assert result >= 0.0

# Specification 2: Result is exactly the average of absolute deviations from the mean
mean = sum(numbers) / len(numbers)
assert abs(result - sum(abs(x - mean) for x in numbers) / len(numbers)) < 1e-12

# Specification 3: MAD is zero if and only if all elements are identical
all_equal = all(x == numbers[0] for x in numbers)
assert (result == 0.0) == all_equal

# Specification 4: Scaling property — multiplying all values by a positive constant c scales MAD by c
c = 3.7  # example positive constant
scaled_numbers = [c * x for x in numbers]
scaled_result = mean_absolute_deviation(scaled_numbers)
assert abs(scaled_result - c * result) < 1e-12

# Specification 5: Translation invariance — adding a constant to all elements does not change MAD
d = -12.4  # arbitrary constant
shifted_numbers = [x + d for x in numbers]
shifted_result = mean_absolute_deviation(shifted_numbers)
assert abs(shifted_result - result) < 1e-12