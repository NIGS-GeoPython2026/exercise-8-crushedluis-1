import math
import numpy as np

def mean(x):
    total = 0
    n = len(x)

    for value in x:
        total += value

    return total / n


def stddev(x):
    x_mean = mean(x)
    total = 0
    n = len(x)

    for value in x:
        total += (value - x_mean) ** 2

    variance = total / (n - 1)
    return math.sqrt(variance)


def sem(x):
    return stddev(x) / math.sqrt(len(x))


def gaussian(x_bar, sigma_x, x):
    x = np.array(x)
    return (1 / (sigma_x * np.sqrt(2 * np.pi))) * np.exp(-((x - x_bar) ** 2) / (2 * (sigma_x ** 2)))

