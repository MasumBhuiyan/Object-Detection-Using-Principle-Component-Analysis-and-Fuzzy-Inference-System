# Object Detection Using Principle Component Analysis and Fuzzy Inference System ![Completeness](https://img.shields.io/badge/completeness-0.6-green.svg) ![Language](https://img.shields.io/badge/python-3.7-blue.svg)

## Table of Contents
1. [ Description ](#description)
2. [ Installation ](#installation)
3. [ Credits ](#credits)
4. [ License ](#license)
5. [ Conclusion ](#conclusion) 

<a name="description"></a>
## Description
It is an object detection system that uses a combination of feature extraction technique and fuzzy inference engine. We choose **principle component analysis** for feature extraction. The system is basically a classification model that determines the similarity between the train images and test images. It selects **k** principle components from a set of train images, calculates their weights, then models the pca to a set of test images. A fuzzy inference engine is built over the weights. The fuzzy output classifies the test images into two classes zero-one. 1 indicates the existence of a certein property, 0 otherwise. <br><br>
**Applications**
* facial recognition
* computer vision
* pattern finding
---
<a name="installation"></a>
## Installation ![os](https://img.shields.io/badge/os-linux-orange) ![editor](https://img.shields.io/badge/sublime_text-3-blue)
* Install **python 3** if not installed. <br>
To install open terminal `Ctrl+Alt+T` and type the following commands<br>
> `$ sudo apt-get update` <br>
> `$ sudo apt-get install python3.7` <br>
> `$ python --version` <br>
* Clone the repository by the following command <br>
> `git clone [repository url]` <br>
* Open the repository with **sublime text 3**
* Open file **__main__.py** <br> 
* Run the program by `Cntrl+B` <br>
---
<a name="credits"></a>
## Credits
<table style="width:100%">
  <tr>
    <td> 
      <b>Masum Bhuiyan</b> <br>
      Jahangirnagar University <br>
      Dhaka, Bangladesh
    </td>
  </tr>
  <tr>
    <td> 
      <b>Omor Faruque Abir</b> <br>
      Jahangirnagar University <br>
      Dhaka, Bangladesh
    </td>
  </tr>
</table>

<a name="license"></a>
## Lincense ![license](https://img.shields.io/badge/license-MIT-green) <br>
MIT License

Copyright (c) 2020 MasumBhuiyan

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.
<a name="conclusion"></a>
## Conclusion
Checkout the [wiki](https://www.demo.com) for detail description of the project.

<a name="license"></a>
## Lincense ![license](https://img.shields.io/badge/license-MIT-green) <br>
MIT License

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.
<a name="conclusion"></a>
## Conclusion
Checkout the [wiki](https://www.demo.com) for detail description of the project.
