from scipy import signal
import numpy as np


# filters an xn signal with lower and upper band frequencies
def bandpass_signal(xn, lower, upper):
    length = len(xn)
    t = np.linspace(-1, 1, length)

    b, a = signal.butter(3, [lower, upper], btype="bandpass", fs=100)

    zi = signal.lfilter_zi(b, a)

    z, _ = signal.lfilter(b, a, xn, zi=zi * xn[0])
    z2, _ = signal.lfilter(b, a, z, zi=zi * z[0])
    y = signal.filtfilt(b, a, xn)

    return y


def standardize(x):
    """Standardize the original data set."""
    mean_x = np.mean(x, axis=0)
    x = x - mean_x
    std_x = np.std(x, axis=0)
    x = x / std_x
    return x, mean_x, std_x


# function to handle nans in feature
def handle_nans(array):
    """shifts the nan values to the mean of the other defined values"""
    # We compute the mean of all values except nan
    # nan values are values that are not equal to themselves
    temp = [[1, x] if x == x else [0, 0] for x in array]

    sum_columns = np.sum(temp, axis=0)
    mean_of_array_without_nan = sum_columns[1] / sum_columns[0]
    for i in range(len(array)):
        if array[i] != array[i]:
            array[i] = mean_of_array_without_nan