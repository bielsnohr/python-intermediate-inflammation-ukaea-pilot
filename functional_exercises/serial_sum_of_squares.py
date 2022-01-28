import pytest
from functools import reduce

def sum_of_squares(sequence):
    squares = [x * x for x in sequence]
    return reduce(lambda a, b: a + b, squares)


@pytest.mark.parametrize("sequence, expected",
                         (
                                 ([1, 2, 3], 14), ([-1, -2, -3], 14)
                         ))
def test_sum_of_squares(sequence, expected):
    assert sum_of_squares(sequence) == expected


sequence = [i for i in range(10000)]
print(sum_of_squares(sequence))
