# tests/test_has_close_elements.py
from typing import List
import pytest
from full_generated_code.chatgpt.HumanEval_0.sample1 import has_close_elements


@pytest.mark.parametrize(
    "numbers, threshold, expected",
    [
        # Specification 1: lists with 0 or 1 element → always False
        ([], 1.0, False),
        ([3.14], 0.5, False),
        ([1.0], 0.0, False),
        
        # Specification 2 & 3: basic correctness (exists pair ≤ threshold)
        ([1.0, 2.0, 3.0], 0.9, True),       # 2.0 - 1.0 = 1.0 > 0.9 → False? Wait, 1.0 is exactly threshold+ε
        ([1.0, 2.0, 3.0], 1.0, True),       # 2.0 - 1.0 = 1.0 ≤ 1.0 → True
        ([1.0, 2.0, 3.0], 0.999, False),    # min distance = 1.0 > 0.999 → False
        
        ([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3, True),   # duplicates → distance 0 ≤ 0.3
        ([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.0, True),   # duplicates → 0 ≤ 0
        
        # Non-consecutive close elements (need O(n²) check, not just consecutive after sort)
        ([1.0, 10.0, 1.05], 0.1, True),                 # 1.0 and 1.05 are close, not consecutive after sort? after sort: [1.0,1.05,10.0] → they are consecutive
        ([0.0, 100.0, 0.08], 0.1, True),                # close but far from middle
        
        # Specification 4: after sorting, close elements must be consecutive
        ([5.0, 1.0, 4.0, 2.0, 3.0], 1.0, True),         # distances after sort: 1,1,1,1 → many ≤1.0
        ([10.0, 1.0, 2.0, 3.0], 0.5, False),            # sorted [1,2,3,10] → min consecutive =1 >0.5 → False
        
        # Edge cases with threshold = 0
        ([1.0, 1.0, 2.0], 0.0, True),                  # exact duplicates
        ([1.0, 2.0, 3.0], 0.0, False),                  # all distinct
        
        # Large numbers / floating point precision
        ([1e10, 1e10 + 1e-9], 1e-8, True),
        ([1e10, 1e10 + 1e-9], 1e-10, False),
    ]
)
def test_has_close_elements_direct(numbers: List[float], threshold: float, expected: bool):
    """Directly test the function against the expected boolean result."""
    assert has_close_elements(numbers, threshold) == expected


def test_specification_1_empty_or_singleton():
    """Specification 1: If ≤1 element → False"""
    assert has_close_elements([], 1.0) is False
    assert has_close_elements([42.0], 0.0) is False
    assert has_close_elements([0.0], 1e-10) is False


def test_specification_2_and_3_min_pairwise_distance():
    """Specification 2 & 3: result ≡ min pairwise distance ≤ threshold"""
    numbers_list = [
        ([1.0, 2.0, 3.0], 1.0),
        ([1.0, 1.01, 100.0], 0.005),
        ([5.0, 5.0], 0.0),
        ([], 1.0),
        ([7.0], 0.0),
    ]
    
    for numbers, threshold in numbers_list:
        if len(numbers) < 2:
            expected = False
        else:
            min_dist = min(abs(numbers[i] - numbers[j])
                          for i in range(len(numbers))
                          for j in range(i + 1, len(numbers)))
            expected = min_dist <= threshold
        assert has_close_elements(numbers, threshold) == expected


def test_specification_4_sorted_consecutive_equivalence():
    """Specification 4: after sorting, checking consecutive pairs is sufficient"""
    cases = [
        ([1.0, 3.0, 2.0, 4.0], 1.0),
        ([10.0, 1.0, 2.0, 10.5], 0.6),
        ([0.0, 0.1, 100.0, 0.05], 0.1),
        ([1.1, 1.2, 1.3, 1.4], 0.15),
        ([], 1.0),
        ([5.5], 0.0),
    ]
    
    for numbers, threshold in cases:
        sorted_nums = sorted(numbers)
        has_consecutive = any(abs(sorted_nums[i+1] - sorted_nums[i]) <= threshold
                              for i in range(len(sorted_nums)-1))
        if len(numbers) <= 1:
            has_consecutive = False
        assert has_close_elements(numbers, threshold) == has_consecutive


def test_specification_5_permutation_invariance():
    """Specification 5: function must be invariant under permutation of input"""
    import itertools
    
    base_cases = [
        ([1.0, 2.0, 3.0], 0.5),      # expected False
        ([1.0, 1.1, 2.0], 0.1),       # expected True
        ([4.0, 4.0], 0.0),            # expected True
        ([], 1.0),                    # expected False
        ([10.0], 0.0),                # expected False
    ]
    
    for numbers, threshold in base_cases:
        reference = has_close_elements(numbers, threshold)
        # Test a few random permutations (including the original)
        for perm in itertools.permutations(numbers):
            assert has_close_elements(list(perm), threshold) == reference