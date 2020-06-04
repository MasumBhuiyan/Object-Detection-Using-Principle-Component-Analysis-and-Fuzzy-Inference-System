import numpy as np

c1 = [8.0,12.0,17.0,18.0]
c2 = [3.0,7.0,9.0,10.0]

def fuzzy_membership(val, dividing_points):
    f = np.zeros(3)
    if val <= dividing_points[0]: 
        f[ 0 ] = 1.0
    elif val <= dividing_points[1]:
        f[ 0 ] = 0.5
        f[ 1 ] = 0.5
    elif val <= dividing_points[2]:
        f[ 1 ] = 1.0
    elif val <= dividing_points[3]:
        f[ 1 ] = 0.5
        f[ 2 ] = 0.5
    else:
        f[ 2 ] = 1.0
    return f;

def engine(mf1, mf2):
    C = LC = D = 0
    C = min(mf1[0],mf2[0]) + min(mf1[0],mf2[1])
    D = min(mf1[2],mf2[1]) + min(mf1[2],mf2[2])
    LC = min(mf1[1],mf2[0]) + min(mf1[2],mf2[0]) + min(mf1[1],mf2[1]) + min(mf1[1],mf2[2]) + min(mf1[0],mf2[2])
    return C, LC, D

def fuzzy_decision(C, LC, D):
    FD = (0.25 * C + 0.5 * LC + 0.75 * D)
    if FD <= 0.5:
        return 1
    return 0

def Run(n, test_weight):
    matches = 0
    test_weight = abs(test_weight)
    for i in range(n):
        v1 = test_weight[0,i]
        v2 = test_weight[1,i]
        mf1 = fuzzy_membership(v1,c1)
        mf2 = fuzzy_membership(v2,c2)
        C, LC, D = engine(mf1, mf2)
        FD = fuzzy_decision(C,LC,D)
        yes = 0
        if i < 10 and FD == 1: 
            yes = 1
        elif i >= 10 and FD == 0:
            yes = 1
        matches += yes
    accuracy = matches / n * 100.0
    print("Accuracy:", accuracy, "%")