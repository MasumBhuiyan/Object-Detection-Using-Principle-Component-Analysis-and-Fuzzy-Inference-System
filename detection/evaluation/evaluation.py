import numpy as np

def euclidian_distance(train_weight, test_weight):
    cst = train_weight - test_weight
    cst = np.multiply(cst, cst)
    cst = np.sum(cst, axis=0)
    cst = np.sqrt(cst)
    return cst.real

def error_function(n, train_weight, test_weight):
    test_weight = test_weight.T
    error = []
    for i in range(n):
        D = test_weight[ i ].T
        D = np.around(euclidian_distance(train_weight, D),2)
        indx = np.argmin(D)
        error.append(indx)
    return np.asarray(error)


def result(n, train_weight, test_weight):
    errors = np.around(error_function(n, train_weight, test_weight),2)
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