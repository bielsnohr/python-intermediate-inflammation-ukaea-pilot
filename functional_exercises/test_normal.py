import numpy as np
from functools import reduce


def test_normal_sampling():
    """Test whether the function for sampling the normal distribution is
    working"""
    mean = 2
    std_dev = 0.1
    size = 1000
    for i in range(10):
        samp = np.random.normal(mean, std_dev, size)
        np.testing.assert_almost_equal(samp.mean(), mean, decimal=2)


def
