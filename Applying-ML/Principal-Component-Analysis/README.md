# How to do do PCA

## 1. By Hand

1. convert data to matrix
2. calculate covariance matrix

    1. calculate means
    2. calculates variances
    3. calculate covariance
    4. put in covariance matrix

3. get eigenvalues
4. get eigenvectors

## 2. Using Numpy

```
import numpy as np

# create a numpy array that stores the data matrix
matrix = np.array([[]])

# calculate the covariance matrix
covariance_matrix = np.cov(matrix[:,0], matrix[:,1])

# create variables to store the Eigen values and Eigen vectors
eigen_values, eigen_vectors = np.linalg.eig(covariance_matrix)
```

## 3. Usng sklearn

```
from sklearn.decomposition import PCA
import pandas as pd

# create and fit a PCA model
pca = PCA(n_components=2)
pca.fit(matrix)

# show the Eigen vector
pca.components_

# show the Eigen values
pca.explained_variance_
```
