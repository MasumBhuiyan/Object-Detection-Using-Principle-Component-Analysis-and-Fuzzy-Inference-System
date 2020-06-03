import numpy as np
from data import io

def pca(k, trainset):
    shi = np.asmatrix(trainset.mean(axis = 1)).T
    phi = trainset - shi
    covariance = np.dot(phi, phi.T)
    eig_vals, eig_vecs = np.linalg.eig(covariance)
    
    i = eig_vals.argsort()[-k:][::-1]
    eig_vals = eig_vals[i]
    component = eig_vecs[:, i]
    
    return component, shi

def flatten(imageset):
    flat = imageset.reshape(imageset.shape[ 0 ], -1).T
    return flat

def weight(U, dataset, shi):
    return np.dot(U.T, dataset - shi)

def train_pca(n, k, size, directory):
    trainset = io.load(n, size, directory)
    print("trainset shape:", trainset.shape)
    
    trainset = flatten(trainset)
    print("trainset shape after flattening:", trainset.shape)
    
    U, shi = pca(k, trainset) 
    print("Principle components:", U.shape)
    print("Average Column Vector:", shi.shape)
    
    train_weight = weight(U, trainset, shi)
    print("Weights of All train data i.e. image:", train_weight.shape)
    
    return U, shi, train_weight

def test_pca(n, size, directory, U, shi, train_weight):
    testset = io.load(n, size, directory)
    print("testset shape:", testset.shape)
    
    testset = flatten(testset)
    print("testset shape after flattening:", testset.shape)
    
    test_weight = weight(U, testset, shi)
    return test_weight
