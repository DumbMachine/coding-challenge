import os
import sys
from functools import reduce

import pytest

sys.path.append(os.path.abspath("."))
from fold_tools import fold, InvalidIterableError


def add(a, b):
    return a + b


def sub(a, b):
    return a - b


def multiply(x, y):
    return x * y


def square(x):
    return x ** 2


def square_root(x):
    return x ** 2


def inverse(x):
    return 1 / x


def test_invalid_iterable():
    with pytest.raises(TypeError):
        fold(None, add)


def test_type_mismatch():
    with pytest.raises(TypeError):
        fold([1, 2], add, "cannot add str to int")


def test_empty_seq_no_init():
    with pytest.raises(InvalidIterableError):
        fold(add, [])


def test_empty_iterable_with_init():
    assert reduce(add, [], 1) == fold(add, [], 1)


def test_empty_seq_none_init():
    fold_result = fold(add, [], None)
    assert None == fold_result
    assert reduce(add, [], None) == fold_result


@pytest.mark.parametrize(
    "func, sequence, accumulator, fold_right",
    [
        (add, [1, 2, 3], 0, False),
        (add, [1, 2, 3], 0, True),
        (sub, [1, 2, 3], 0, False),
        (sub, [1, 2, 3], 0, True),
        (multiply, [1, 2, 3], 0, False),
        (multiply, [1, 2, 3], 0, True),
        (max, [1, 2, 3], 0, False),
        (max, [1, 2, 3], 0, True),
        (min, [1, 2, 3], 0, False),
        (min, [1, 2, 3], 0, True),
        (add, ["taktile", " coding", " challenge"], "", False),
        (add, ["taktile", " coding", " challenge"], "", True),
    ],
)
def test_(func, sequence, accumulator, fold_right):
    fold_result = fold(func, sequence, accumulator, fold_right)
    if fold_right:
        assert fold_result == reduce(func, reversed(sequence), accumulator)
    else:
        assert fold_result == reduce(func, sequence, accumulator)
