import numpy as np
from data import io

'''
flatten(imageset)
    - converts an image to a column vector
'''
def flatten(imageset):
    flat = imageset.reshape(imageset.shape[ 0 ], -1).T
    return flat

'''
weight(U, dataset, shi)
    - calculate weight of each train sample 
    - using first k pca
'''
def weight(U, dataset, shi):
    return np.dot(U.T, dataset - shi)

'''
pca(k, trainset):
    - returns the first k pca
'''
def pca(k, trainset):
    shi = np.asmatrix(trainset.mean(axis = 1)).T
    phi = trainset - shi
    covariance = np.dot(phi, phi.T)
    eig_vals, eig_vecs = np.linalg.eig(covariance)
    
    i = eig_vals.argsort()[-k:][::-1]
    eig_vals = eig_vals[i]
    component = eig_vecs[:, i]
    
    return component, shi

'''
train_pca(n, k, image_size, directory)
    - calculate pca, weight
'''
def train_pca(n, k, image_size, directory):
    trainset = io.load(n, image_size, directory)
    print("trainset shape:", trainset.shape)
    
    trainset = flatten(trainset)
    print("trainset shape after flattening:", trainset.shape)
    
    U, shi = pca(k, trainset) 
    print("Principle components:", U.shape)
    print("Average Column Vector:", shi.shape)
    
    train_weight = weight(U, trainset, shi)
    print("train weight data shape:", train_weight.shape)
    
    return U, shi, train_weight

'''
test_pca(n, image_size, directory, U, shi, train_weight)
    - maps the testset with pca
    - calculates test weights
'''
def test_pca(n, image_size, directory, U, shi, train_weight):
    testset = io.load(n, image_size, directory)
    print("testset shape:", testset.shape)
    
    testset = flatten(testset)
    print("testset shape after flattening:", testset.shape)
    
    test_weight = weight(U, testset, shi)
    return test_weight
