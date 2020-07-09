from data import io
from pca import pca
from fis import fuzzification
from evaluation import evaluation
from ga import geneticalgorithm as ga
components = 2
image_size = (32,32)
trainset_size = 20
testset_size = 20

train_directory = "./resources/trainset/image"
test_directory =  "./resources/testset/image"

def run_pca():
	U, shi, train_weight = pca.train_pca(trainset_size, components, image_size, train_directory)
	test_weight = pca.test_pca(testset_size,image_size,test_directory, U, shi, train_weight)
	evaluation.accuracy(testset_size, train_weight, test_weight)
	return train_weight, test_weight

train_weight, test_weight = run_pca()
#fuzzification.Run(testset_size,test_weight)
input('Press enter to run GA.\n')
ga.Run(testset_size,test_weight)
input('program finished, press enter to quit.\n')
