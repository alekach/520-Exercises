import pytest

from seeded_code.grok.HumanEval_4.sample2 import mean_absolute_deviation as candidate



METADATA = {
    'author': 'jt',
    'dataset': 'test'
}


def check(candidate):
    assert abs(candidate([1.0, 2.0, 3.0]) - 2.0/3.0) < 1e-6
    assert abs(candidate([1.0, 2.0, 3.0, 4.0]) - 1.0) < 1e-6
    assert abs(candidate([1.0, 2.0, 3.0, 4.0, 5.0]) - 6.0/5.0) < 1e-6



def test_check():
    check(candidate)


def test_empty_list():
    with pytest.raises(ValueError) as exc_info:
        candidate([])
    assert str(exc_info.value) == "Input list cannot be empty"