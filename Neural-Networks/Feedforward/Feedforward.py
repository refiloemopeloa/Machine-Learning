import numpy as np

def get_input(input_size):
    a = np.array([])

    for i in range(input_size):
        ai = float(input())
        a = np.append(a, ai)

    return a

def get_weights(input_size, layer_size):
    W = np.zeros((input_size, layer_size))

    for i in range(input_size):
        W[i] = np.random.uniform(-1, 1, size=layer_size)

    return W

def get_biases(layer_size):
    return np.reshape(np.random.uniform(-1, 1, size=(layer_size,1)), layer_size)

def sigmoid(x):
    return 1 / (1 + np.exp(-x))
