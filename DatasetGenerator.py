import imageio as iio
import numpy as np
import os

# Initialize the data matrix and the label vector
dataMatrix = []
labelVector = []

dataMatrixNonFaces = []
labelVectorNonFaces = []

# The path for the 'archive' directory we downloaded, 
# that is, the directory which contains sub-directories named from s1 to s40
mainDirectory = "/home/mohamed/CSED_25/Year_3/term_2/PR-ML/my_labs/lab_1/faces"
NonFacesDirectory = 'D:\\CSED\\semester-6\\pattern-recognetion\\labs\\lab1-faceRecognition\\faces'
# mainDirectory = 'D:\\CSED\\semester-6\\pattern-recognetion\\labs\\lab1-faceRecognition\\faces'

def generateData():
    # Iterate the sub-directories, and load each set of images as 10 (number of images for each subject) 
    # 1-d vectors (using np.ravel) into the data matrix
    for subDirectory in sorted(os.listdir(mainDirectory)):
        path = os.path.join(mainDirectory, subDirectory)
        if os.path.isdir(path):
            for image in sorted(os.listdir(path)):
                dataMatrix.append(np.ravel(iio.imread(os.path.join(path, image))))
                # Fill up the label vector --> We can concatanate this to the data matrix if we needed
                labelVector.append(int(subDirectory[1:3]))
    return dataMatrix, labelVector

def generateDataNonFace():  # 400 faces and 800 nonfaces
    # Iterate the sub-directories, and load each set of images as 10 (number of images for each subject) 
    # 1-d vectors (using np.ravel) into the data matrix
    # global NonFacesDirectory
    # for subDirectory in os.listdir(mainDirectory):
    #     path = os.path.join(mainDirectory, subDirectory)
    #     if os.path.isdir(path):
    #         for image in os.listdir(path):
    #             dataMatrixNonFaces.append(np.ravel(iio.imread(os.path.join(path, image))))
    #             # Fill up the label vector --> We can concatanate this to the data matrix if we needed
    #             labelVectorNonFaces.append(1)   # 1 for faces, 2 for non-faces
    # for image in os.listdir(NonFacesDirectory):
    #     dataMatrixNonFaces.append(np.ravel(iio.imread(os.path.join(NonFacesDirectory, image))))
    #     # Fill up the label vector --> We can concatanate this to the data matrix if we needed
    #     labelVectorNonFaces.append(2)
    # return dataMatrixNonFaces, labelVectorNonFaces
    return [],[]