import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6])

window_size = 3

shape = (arr.shape[0] - window_size + 1, window_size)
strides = (arr.strides[0], arr.strides[0])

windows = np.lib.stride_tricks.as_strided(arr, shape=shape, strides=strides)

moving_avg = windows.mean(axis=1)

print(moving_avg)
