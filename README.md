# Object Detection Using Principle Component Analysis and Fuzzy Inference System ![Completeness](https://img.shields.io/badge/completeness-0.5-green.svg) ![Language](https://img.shields.io/badge/python-3.7-blue.svg)

## Description: 
An object detection system that uses a combination of feature extraction technique i.e **PCA** and fuzzy inference engine. It is a classification model that determines the similarity between the train images and test images. It selects **k** principle components from a set of train images, calculates their weights, then models the pca to a set of test images. A fuzzy inference engine is built over the weights. The fuzzy output classifies the test images into two classes zero-one. 1 indicates the existence of a certein property, 0 otherwise. <br><br>
**Applications:**
* facial recognition
* computer vision
* pattern finding

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
