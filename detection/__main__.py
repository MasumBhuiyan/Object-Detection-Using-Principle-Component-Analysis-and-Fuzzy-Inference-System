from data import io
from pca import pca
from evaluation import evaluation

U, shi, train_weight = pca.train_pca(20, 4, (32,32), "./resources/trainset/image")
test_weight = pca.test_pca(20,(32,32),"./resources/testset/image", U, shi, train_weight)
evaluation.accuracy(20, train_weight, test_weight)