# Object Detection Using Principle Component Analysis and Fuzzy Inference System ![Completeness](https://img.shields.io/badge/completeness-0.5-green.svg) ![Language](https://img.shields.io/badge/python-3.7-blue.svg)

## Description: 
An object detection system that uses a combination of feature extraction technique i.e **PCA** and fuzzy inference engine. <br> <br>
**Algorithm** <br>
* Read, resize, and pixelize a set of train images
* Convert each train image into a column vector 
* Make a matrix using the column vectors where each column is an train image
* Calculate pca over the previously formed matrix
* Calculate a weight matrix of the train images using the pca matrix
* Read, resize, and pixelize a set of test images
* Calculate another weight matrix for test images using the above calculated pca matrix
* Define a fuzzy inference system over weight values (If-else rules)
* Pass the weight matrix of the test images to fuzzy inference system
* take the fuzzy output and calculate accuracy of the model

 **Directory Structure**<br>
```
.
├── detection
│   ├── data
│   │   ├── __init__.py
│   │   └── __init__.pyc
│   ├── evaluation
│   │   ├── evaluation.py
│   │   └── __init__.py
│   ├── fis
│   │   └── __init__.py
│   ├── __init__.py
│   ├── __main__.py
│   ├── pca
│   │   ├── __init__.py
│   │   └── pca.py
│   └── resources
│       ├── testdata
│       │   ├── image1.jpeg
│       │   ├── image2.jpeg
│       │   ├── image3.jpeg
│       │   ├── image4.jpeg
│       │   └── image5.jpeg
│       └── traindata
│           ├── image1.jpeg
│           ├── image2.jpeg
│           ├── image3.jpeg
│           ├── image4.jpeg
│           └── image5.jpeg
├── LICENSE
└── README.md
```

## Table of Contents

## Installation ![os](https://img.shields.io/badge/os-linux-orange) ![editor](https://img.shields.io/badge/sublime_text-3-blue)
* Install ![cmake](https://img.shields.io/badge/python-3.7-blue) if not installed. <br>
To install open terminal `Ctrl+Alt+T` and type the following commands<br>
> `$ sudo apt-get update` <br>
> `$ sudo apt-get install python3.7` <br>
> `$ python --version` <br>
* Clone the repository by the following command <br>
> `git clone [repository url]` <br>
* Open the repository with ![editor](https://img.shields.io/badge/sublime_text-3-blue) <br>
* Open file **__main__.py** <br> 
* Run the program by `Cntrl+B` <br>

## Usage:

## Contributing

## Credits

## Lincense
