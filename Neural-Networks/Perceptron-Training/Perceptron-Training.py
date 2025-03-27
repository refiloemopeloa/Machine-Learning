import numpy as np

def make_dataset(N,m=2):
    X = np.empty(shape=(N,m),dtype=int)

    for row in range(N):
        row_entry = np.random.randint(0,2,(1,m))
        X[row] = row_entry

    return X

def make_targets(N):
    T = np.empty(shape=(N,1),dtype=int)

    for row in range(N):
        row_entry = np.random.randint(0,2,(1,1))
        T[row] = row_entry

def main():
    N = int(input("N:\t"))
    m = int(input("m:\t"))

    X = make_dataset(N,m)

    print(X)

if __name__ == '__main__':
    main()