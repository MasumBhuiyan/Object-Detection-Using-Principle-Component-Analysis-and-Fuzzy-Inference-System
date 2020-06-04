import numpy as np

'''
distance(A, B)
    - returns the euclidean distance of two array
'''
def distance(A, B):
    C = A - B
    return (np.sqrt(np.sum(np.multiply(C, C),axis=0))).real;

'''
error(n, train, test)
    - for each test sample return the index of the min error 
'''
def error(n, train_weight, test_weight):
    test_weight = test_weight.T
    error = []
    for i in range(n):
        D = test_weight[ i ].T
        D = np.around(distance(train_weight, D),2)
        indx = np.argmin(D)
        error.append(indx)
    return np.asarray(error)

'''
accuracy(n, train_weight, test_weight)
    - prints percentage of correct prediction
'''
def accuracy(n, train_weight, test_weight):
    errors = np.around(error(n, train_weight, test_weight),2)
    matches = 0
    for i in range(n):
        val = 0
        if i < 10 and errors[ i ] < 10: 
            val = 1
        if i >= 10 and errors[ i ] >= 10:
            val = 1
        matches += val
    accuracy = matches / n * 100.0
    print("Accuracy:", accuracy, "%")