import numpy as np

def get_input(input_size):
    a = np.array([])

    for i in range(input_size):
        ai = float(input())
        a = np.append(a, ai)

    return a
