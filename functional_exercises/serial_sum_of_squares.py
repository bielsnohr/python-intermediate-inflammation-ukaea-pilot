import pytest
from functools import reduce


def sum_of_squares(sequence):
    squares = [x * x for x in sequence]
    return reduce(lambda a, b: a + b, squares)


def to_integer(sequence):
    return [int(x) for x in sequence]


def remove_comments(sequence):
    return [x for x in sequence if x[0] != "#"]


@pytest.mark.parametrize("sequence, expected", (([1, 2, 3], 14), ([-1, -2, -3], 14)))
def test_sum_of_squares(sequence, expected):
    assert sum_of_squares(sequence) == expected


@pytest.mark.parametrize(
    "sequence, expected",
    ((["1", "2", "3"], 14), (["-1", "-2", "-3"], 14), (["#100", "1", "2", "3"], 14)),
)
def test_filtered_sum_of_squares(sequence, expected):
    assert sum_of_squares(to_integer(remove_comments(sequence))) == expected


sequence = [i for i in range(10000)]
print(sum_of_squares(sequence))
