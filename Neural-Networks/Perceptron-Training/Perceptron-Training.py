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


def main():
    N = int(input("N:\t"))
    m = int(input("m:\t"))

    X = make_dataset(N,m)

    print(X)

if __name__ == '__main__':
    main()