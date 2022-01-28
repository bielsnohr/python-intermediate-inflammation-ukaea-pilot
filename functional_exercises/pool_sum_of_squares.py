import pytest
from functools import reduce
from multiprocessing.pool import Pool


def product(x):
    return x * x


# TODO this isn't yielding any performance gain. Investigate!
def sum_of_squares(sequence):
    with Pool(processes=6) as pool:
        squares = pool.map(product, sequence)
    return reduce(lambda a, b: a + b, squares)


@pytest.mark.parametrize("sequence, expected",
                         (
                                 ([1, 2, 3], 14), ([-1, -2, -3], 14)
                         ))
def test_sum_of_squares(sequence, expected):
    assert sum_of_squares(sequence) == expected


sequence = [i for i in range(10000)]
print(sum_of_squares(sequence))
