import numpy as np
import matplotlib.pyplot as plt
from PIL import Image, ImageOps

'''
read(directory)
	- reads an image from directory
'''
def read(directory):
	return Image.open(directory)

'''
resize(image, image_size)
	- resize image by image_size i.e. (32,32)
'''
def resize(image, image_size):
	return ImageOps.fit(image, image_size, Image.ANTIALIAS)

'''
pixelize(image)
	- gives pixel values of the image
'''
def pixelize(image):
	return  np.array(image.getdata()).reshape(image.size[0], image.size[1], 3) / 255

'''
load(n, image_size, directory)
	- reads n images from directory. 
	- resize by image_size
	- then pixelize
	- return all the pixelized images  
'''
def load(n, image_size, directory):
	print("loading data...")
	images = []
	for i in range(n):
		image = pixelize(resize(read(directory + str(i + 1) + ".jpeg"), image_size))
		images.append(image)
	print("loaded successfully!!!")
	return np.asarray(images)

'''
display(r, c, images)
	- print (r x c) plots to display images
'''
def display(r, c, images):
    n = images.shape[0]
    fig = plt.figure(figsize=(20,10))
    for i in range(n):
        fig.add_subplot(r, c, i + 1)
        plt.imshow(images[ i ])
