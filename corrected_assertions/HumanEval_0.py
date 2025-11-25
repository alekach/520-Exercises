from typing import List
from full_generated_code.chatgpt.HumanEval_0.sample1 import has_close_elements

numbers: List[float]
threshold: float
result = has_close_elements(numbers, threshold)   # this is the value returned by the function

# Specification 1: If the list has 0 or 1 element, no two distinct elements can be close
if len(numbers) <= 1:
    assert result == False

# Specification 2: If there exist two distinct elements whose absolute difference is less than or equal to threshold,
#           the function must return True (most direct correctness property)
exists_pair = any(
    i < j and abs(numbers[i] - numbers[j]) <= threshold
    for i in range(len(numbers))
    for j in range(i + 1, len(numbers))
)
assert result == exists_pair

# Specification 3: Equivalence with the "min pairwise distance" view
#           The function returns True iff the minimum absolute distance between any two distinct elements ≤ threshold
if len(numbers) >= 2:
    min_distance = min(
        abs(numbers[i] - numbers[j])
        for i in range(len(numbers))
        for j in range(i + 1, len(numbers))
    )
    assert result == (min_distance <= threshold)
else:
    assert result == False

# Specification 4: After sorting, close elements appear in consecutive positions if any exist
sorted_nums = sorted(numbers)
has_consecutive_close = any(
    abs(sorted_nums[k+1] - sorted_nums[k]) <= threshold
    for k in range(len(sorted_nums) - 1)
)
assert result == has_consecutive_close

# Specification 5: The function is invariant under permutation of the input list
import itertools
for perm in itertools.permutations(numbers):
    perm_result = any(
        i < j and abs(list(perm)[i] - list(perm)[j]) <= threshold
        for i in range(len(list(perm)))
        for j in range(i + 1, len(list(perm)))
    )
    assert perm_result == result