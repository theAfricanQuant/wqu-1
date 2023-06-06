import numpy as np

def arithmetic_mean(numpy_array):
    return sum(numpy_array) / numpy_array.count()

def geometric_mean(numpy_array):
    return np.prod(numpy_array)