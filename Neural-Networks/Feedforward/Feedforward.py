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

def activation_function(x, function):
    if function == 'sigmoid':
        return sigmoid(x)

def feedforward(a, W, b, function):
    aW = np.matmul(a,W)
    aWb = aW + b
    return activation_function(aWb, function)

def print_output(a):
    for ai in a:
        print(ai, end=' ')
    print()

def main():
    input_size = int(input("Enter the input size:\n"))
    # input_size = 2
    print("Enter the inputs:")
    a0 = get_input(input_size)
    # a0 = np.array([2,1])
    print("Input:")
    print_output(a0)

    hidden_layer_size = int(input("Enter the hidden layer size:\n"))+1

    for layer in range(hidden_layer_size):
        layer_size = int(input("Enter the layer size:\n"))
        # layer_size = 3
        W = get_weights(input_size, layer_size)
        # W = [[[2, 1, -1],
        #               [-2, -4, 1]],
        #              [[-2,3],
        #               [3,-1],
        #               [5,0]]]
        b = get_biases(layer_size)
        # b1 = np.array([1,-1,2])
        # b = [[1,-1,2], [0,-1]]

        function = 'sigmoid'
        a1 = feedforward(a0, np.array(W[layer]), b[layer], function)

        print("Output:")
        print_output(a1)
        a0=a1

if __name__ == '__main__':
    main()
