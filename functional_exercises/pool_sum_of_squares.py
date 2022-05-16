import pytest
from functools import reduce
from multiprocessing.pool import Pool

def sum_of_squares(sequence):
    """The non-parallel version"""
    squares = [x * x for x in sequence]
    return reduce(lambda a, b: a + b, squares)


def product(x):
    return x * x


# TODO this isn't yielding any performance gain. Investigate!
def pool_sum_of_squares(sequence):
    """The multiprocessing version"""
    with Pool(processes=6) as pool:
        squares = pool.map(product, sequence)
    return reduce(lambda a, b: a + b, squares)


@pytest.mark.parametrize("sequence, expected",
                         (
                                 ([1, 2, 3], 14), ([-1, -2, -3], 14)
                         ))
def test_sum_of_squares(sequence, expected):
    assert sum_of_squares(sequence) == expected
    assert pool_sum_of_squares(sequence) == expected


if __name__ == "__main__":
    import timeit
    sequence = [i for i in range(10000)]
    numb = 1000
    print(timeit.timeit("sum_of_squares(sequence)", globals=globals(),
                        number=numb))
    print(timeit.timeit("pool_sum_of_squares(sequence)", globals=globals(),
                  number=numb))
