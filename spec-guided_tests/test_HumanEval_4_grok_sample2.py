import pytest
from typing import List
from full_generated_code.grok.HumanEval_4.sample2 import mean_absolute_deviation


def test_mean_absolute_deviation_basic_cases():
    assert mean_absolute_deviation([1.0, 2.0, 3.0, 4.0]) == 1.0
    assert mean_absolute_deviation([1.0, 1.0, 1.0]) == 0.0
    assert mean_absolute_deviation([0.0, 0.0, 0.0, 0.0]) == 0.0
    assert mean_absolute_deviation([-1.0, 0.0, 1.0]) == pytest.approx(2.0 / 3.0)


def test_non_negativity():
    # MAD must always be >= 0
    test_cases = [
        [1.0],
        [1.5, 2.5],
        [-5.0, -5.0, -5.0],
        [0.0, 10.0, -10.0, 20.0],
        [1e10, 1e10 + 1, 1e10 - 1],
    ]
    for numbers in test_cases:
        assert mean_absolute_deviation(numbers) >= 0.0


def test_zero_iff_all_elements_identical():
    test_cases = [
        ([5.0], True),
        ([1.0, 1.0, 1.0], True),
        ([0.0, 0.0, 0.0, 0.0], True),
        ([1.0, 2.0], False),
        ([1.0, 1.0, 1.000001], False),
        ([-1.0, -1.0, -1.0, -1.0], True),
        ([1.5, 2.5, 3.5], False),
    ]
    for numbers, should_be_zero in test_cases:
        result = mean_absolute_deviation(numbers)
        if should_be_zero:
            assert result == pytest.approx(0.0)
        else:
            assert result > 0.0


def test_exact_definition_average_absolute_deviation():
    def reference_mad(numbers: List[float]) -> float:
        if not numbers:
            return 0.0
        mean = sum(numbers) / len(numbers)
        return sum(abs(x - mean) for x in numbers) / len(numbers)

    test_cases = [
        [1.0, 2.0, 3.0],
        [10.0],
        [1.0, 1.0, 1.0, 1.0],
        [-2.0, -1.0, 0.0, 1.0, 2.0],
        [0.1, 0.2, 0.3, 0.4, 0.5],
        [1000000.0, 1000001.0, 999999.0],
    ]
    for numbers in test_cases:
        expected = reference_mad(numbers)
        actual = mean_absolute_deviation(numbers)
        assert abs(actual - expected) < 1e-12


def test_scaling_property_positive_constant():
    constants = [2.0, 3.7, 0.5, 100.0, 1e-5]
    base_lists = [
        [1.0, 2.0, 3.0, 4.0],
        [-1.0, 0.0, 1.0],
        [10.0],
        [0.0, 5.0, -5.0],
    ]
    for c in constants:
        for numbers in base_lists:
            original_mad = mean_absolute_deviation(numbers)
            scaled = [c * x for x in numbers]
            scaled_mad = mean_absolute_deviation(scaled)
            assert abs(scaled_mad - c * original_mad) < 1e-12


def test_translation_invariance():
    shifts = [10.0, -12.4, 0.0, 1e6, -999.999]
    base_lists = [
        [1.0, 2.0, 3.0],
        [-5.0, -4.0, -3.0],
        [0.0],
        [1.1, 2.2, 3.3, 4.4],
    ]
    for d in shifts:
        for numbers in base_lists:
            original_mad = mean_absolute_deviation(numbers)
            shifted = [x + d for x in numbers]
            shifted_mad = mean_absolute_deviation(shifted)
            assert abs(shifted_mad - original_mad) < 1e-12


def test_single_element_list():
    # Single element -> mean = element -> all deviations = 0 -> MAD = 0
    for x in [0.0, 1.0, -1.0, 3.14159, -999999.0]:
        assert mean_absolute_deviation([x]) == pytest.approx(0.0)


def test_large_numbers_and_numerical_stability():
    # Test that implementation doesn't suffer from catastrophic cancellation
    large = 1e12
    numbers = [large, large + 1.0, large - 1.0, large + 2.0]
    mad = mean_absolute_deviation(numbers)
    # Mean = large + 0.5, deviations: 0.5, 0.5, 1.5, 1.5 → average = 1.0
    assert abs(mad - 1.0) < 1e-9