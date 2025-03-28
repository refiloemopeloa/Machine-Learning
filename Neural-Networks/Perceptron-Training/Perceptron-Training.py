import numpy as np

def generate_dataset(N,m=2):
    X = np.empty(shape=(N,m),dtype=int)

    for row in range(N):
        row_entry = np.random.randint(0,2,(1,m))
        X[row] = row_entry

    return X

def linear_function(x1, x2):
    return 2*x1 + 3*x2 - 1

def generate_targets(N, dataset):
    T = np.empty(shape=(N,1),dtype=int)

    for row in range(N):
        if linear_function(dataset[row,0],dataset[row,1]) <= 0:
            T[row] = 0
        else:
            T[row] = 1

    return T

def sample_input():
    X = np.array([[0,0],[0,1],[1,0],[1,1]])
    T = np.array([1,1,1,0])

    return X,T

def generate_weights(m):
    weights = np.empty(shape=(m,1),dtype=float)
    for row in range(m):
        weight = np.random.uniform(-1,1)
        weights[row] = weight

    return weights

def generate_threshold():
    return np.random.uniform(-1,1)

def perceptron(x, weights, threshold):
    sum = 0
    for i in range(len(x)):
        sum += x[i] * weights[i]
    if sum > threshold:
        return 1
    else:
        return 0

def loss(t, y):
    return t - y

def train_perceptron(m, N, X, weights, targets, threshold, learning_rate, stop_condition):
    L1 =0
    L2 = 0
    epochs = 0
    while True:
        for i in range(N):
            y = perceptron(X[i,:], weights, threshold)
            for j in range(m):
                weights[j] += learning_rate * (targets[i] - y) * X[i,j]
            threshold -= learning_rate * (targets[i] - y)
            L2 = L1
            L1 += loss(targets[i], y)
        epochs += 1
        if np.abs(L2-L1) <= stop_condition:
            break

    return weights, threshold, epochs

def print_state(weights, threshold):
    print("Weights:\n",weights)
    print("Threshold:\n",threshold)
    print("=====================")

def print_data(X, T):
    print("X\tT")
    for i in range(len(T)):
        print(X[i], "\t", T[i])

def main():
    N = int(input("N:\t"))
    m = int(input("m:\t"))

    X = make_dataset(N,m)

    print(X)

if __name__ == '__main__':
    main()