import numpy as np

'''
flatten(imageset)
    - converts an image to a column vector
'''
def flatten(imageset):
    flat = imageset.reshape(imageset.shape[ 0 ], -1).T
    return flat

'''
weight(pc, imageset, shi)
    - calculate weight of each image in the imageset 
    - using first k principle components
'''
def weight(pc, shi, imageset):
    return np.dot(pc.T, imageset - shi)

'''
pca(k, trainset):
    - returns the first k principle components
'''
def pca(k, trainset):
	#average column vector
    shi = np.asmatrix(trainset.mean(axis = 1)).T
    
    #computes covariance matrix
    phi = trainset - shi
    covariance = np.dot(phi, phi.T)
    
    #computes eigen values and eigen vectors
    eig_vals, eig_vecs = np.linalg.eig(covariance)
    
    #sorts eigen vectors in decreasing order of eigen values
    i = eig_vals.argsort()[-k:][::-1]
    
    #returns k principle components
    eig_vals = eig_vals[i]
    pc = eig_vecs[:, i]
    return pc, shi


'''
train(n, k, trainset, testset)
    - calculates principle components
    - returns train and test weights
'''
def train(n, k, trainset, testset):
    
    #flattens each image in the trainset and testset
    trainset = flatten(trainset)
    testset = flatten(testset)
  	
  	#calculates k principle components and average column vector
    pc, shi = pca(k, trainset) 
   	
   	#calculates weights of the train and test samples
    train_weight = weight(pc, shi, trainset)
    test_weight = weight(pc, shi, testset)
 	
    return train_weight, test_weight