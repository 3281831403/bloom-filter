import pytest

from probabilistic import bloom as mod

CASES = [
    ('hashes', ['a', 3, 16], [12, 15, 2], False),
    ('hashes', ['', 2, 8], [2, 0], False),
    ('add', [[False, False, False, False, False, False, False, False], 'a', 2], [False, False, False, False, True, False, False, True], False),
    ('contains', [[True, True, True, True, True, True, True, True], 'a', 2], True, False),
    ('contains', [[False, False, False, False, False, False, False, False], 'a', 2], False, False),
    ('false_positive_rate', [100, 1000, 3], 0.017410586496326586, True),
    ('union', [[True, False], [False, True]], [True, True], False),
    ('union', [[], []], [], False),
    ('hashes', ['abc', 1, 4], [0], False),
    ('add', [[False, False, False, False], 'x', 1], [True, False, False, False], False),
    ('contains', [[True, True, True, True], 'x', 1], True, False),
    ('false_positive_rate', [0, 100, 3], 0.0, True),
    ('union', [[True], [True]], [True], False),
    ('union', [[False], [False]], [False], False),
    ('add', [[False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False], '', 3], [False, False, False, False, False, False, False, False, True, True, True, False, False, False, False, False], False),
]


@pytest.mark.parametrize("func_name,args,expected,approx", CASES)
def test_bloom_contract(func_name, args, expected, approx):
    func = getattr(mod, func_name)
    result = func(*args)
    if approx:
        assert result == pytest.approx(expected)
    else:
        assert result == expected
