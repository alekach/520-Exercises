import pytest

from full_generated_code.chatgpt.HumanEval_6.sample3 import parse_nested_parens as candidate



METADATA = {
    'author': 'jt',
    'dataset': 'test'
}


def check(candidate):
    assert candidate('(()()) ((())) () ((())()())') == [2, 3, 1, 3]
    assert candidate('() (()) ((())) (((())))') == [1, 2, 3, 4]
    assert candidate('(()(())((())))') == [4]


def test_check():
    check(candidate)
