# Custom-Instance-Segmentation
Image Segmentation is an important field in computer vision, it is applied in different fields of life. PixelLib is a library created to allow easy application of segmentation to real life problems. Segmentation with coco model is limited as you cannot perform segmentation beyond the 80 classes available in coco. 

It is now possible to train your custom objects’ segmentation model with PixelLib Library with just 7 Lines of Code.
## Install PixelLib and its dependencies:

#### Install Tensorflow with:(PixelLib supports tensorflow 2.0 and above)
1. pip install tensorflow
#### Install imgaug with: 
2. pip install imgaug
#### Install PixelLib with
3. pip install pixellib


# The steps required to train a custom model.
## STEP1:
**Prepare your dataset:**
Our goal is to create a model that can perform instance segmentation and object detection on custom images.
Collect images for the objects you want to detect and annotate your dataset for custom training. Labelme is the tool employed to perform polygon annotation of objects. Create a root directory or folder and within it create train and test folder. Separate the images required for training (a minimum of 300) and test. Put the images you want to use for training in the train folder and put the images you want to use for testing in the test folder. 
You will annotate both images in the train and test folder.

## Image Annotation With Labelme
Labelme is one of the most convenient annotation tool for polygon annotation. This article explains how to use labelme for annotation of objects.
Install labelme and its dependencies.
**On Windows:**
pip3 install pyqt5
pip3 install labelme
**On Ubuntu 14.04 / Ubuntu 16.04:**
sudo apt-get install python3-pyqt5
sudo pip3 install labelme

In your PC’s anaconda or command prompt just type labelme and labelme’s GUI will be displayed as a separate window.
