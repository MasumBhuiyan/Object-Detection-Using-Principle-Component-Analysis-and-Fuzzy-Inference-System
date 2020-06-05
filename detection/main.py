import scan
import pca

#no of priciple components
k = 2

#trainset size
n = 20

#testset size
m = 20

#image size
size = (32, 32)

#resource directories
train_directory = "../resources/train/image"
test_directory = "../resources/test/image"

#loading trainset and testset
trainset = scan.load(n, size, train_directory)
testset = scan.load(m, size, test_directory)

#calculates train and test weights
train_weight, test_weight = pca.train(n, k, trainset, testset)

