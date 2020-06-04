from data import io
from pca import pca
from evaluation import evaluation
from fis import fuzzification

U, shi, train_weight = pca.train_pca(20, 2, (32,32), "./resources/trainset/image")
test_weight = pca.test_pca(20,(32,32),"./resources/testset/image", U, shi, train_weight)

print("PCA accuracy:")
evaluation.accuracy(20, train_weight, test_weight)
print("PCA + Fuzzy accuracy:")
fuzzification.Run(20,test_weight)