import DatasetGenerator

dataMatrix, labelVector = DatasetGenerator.generateData()
dataMatrixNonFaces, labelVectorNonFaces = DatasetGenerator.generateDataNonFace()

# Splitting the data into two sets, one for training and one for testing
def splitData():
    trainingData = []
    testingData = []
    trainingLabels = []
    testingLabels = []
    for i in range(len(dataMatrix)):
        # Train for even entries, test for odd entries
        if i % 2 == 0:
            trainingData.append(dataMatrix[i])
            trainingLabels.append(labelVector[i])
        else:
            testingData.append(dataMatrix[i])
            testingLabels.append(labelVector[i])
    return trainingData, trainingLabels, testingData, testingLabels

def splitDataNonFaces():
    trainingData = []
    testingData = []
    trainingLabels = []
    testingLabels = []
    for i in range(len(dataMatrixNonFaces)):
        # Train for the first 200 face images and the first 200 non-face images
        if i < 200 or (i >= 400 and i < 600):
            trainingData.append(dataMatrixNonFaces[i])
            trainingLabels.append(labelVectorNonFaces[i])
        # Test for the second 200 face images and the second 200 non-face images
        elif (i >= 200 and i < 400) or (i >= 600 and i < 800):
            testingData.append(dataMatrixNonFaces[i])
            testingLabels.append(labelVectorNonFaces[i])
    return trainingData, trainingLabels, testingData, testingLabels

def splitDataNonFaces50():
    trainingData = []
    testingData = []
    trainingLabels = []
    testingLabels = []
    for i in range(len(dataMatrixNonFaces)):
        # Train for the first 200 face images and the first 50 non-face images
        if i < 200 or (i >= 400 and i < 450):
            trainingData.append(dataMatrixNonFaces[i])
            trainingLabels.append(labelVectorNonFaces[i])
        # Test for the second 200 face images and the second 200 non-face images
        elif (i >= 200 and i < 400) or (i >= 600 and i < 800):
            testingData.append(dataMatrixNonFaces[i])
            testingLabels.append(labelVectorNonFaces[i])
    return trainingData, trainingLabels, testingData, testingLabels

def splitDataNonFaces100():
    trainingData = []
    testingData = []
    trainingLabels = []
    testingLabels = []
    for i in range(len(dataMatrixNonFaces)):
        # Train for the first 200 face images and the first 100 non-face images
        if i < 200 or (i >= 400 and i < 500):
            trainingData.append(dataMatrixNonFaces[i])
            trainingLabels.append(labelVectorNonFaces[i])
        # Test for the second 200 face images and the second 200 non-face images
        elif (i >= 200 and i < 400) or (i >= 600 and i < 800):
            testingData.append(dataMatrixNonFaces[i])
            testingLabels.append(labelVectorNonFaces[i])
    return trainingData, trainingLabels, testingData, testingLabels

def splitDataNonFaces400():
    trainingData = []
    testingData = []
    trainingLabels = []
    testingLabels = []
    for i in range(len(dataMatrixNonFaces)):
        # Train for the first 200 face images and the first 200 and the third 200 non-face images
        if i < 200 or (i >= 400 and i < 600) or (i >= 800 and i < 1000):
            trainingData.append(dataMatrixNonFaces[i])
            trainingLabels.append(labelVectorNonFaces[i])
        # Test for the second 200 face images and the second 200 non-face images
        elif (i >= 200 and i < 400) or (i >= 600 and i < 800):
            testingData.append(dataMatrixNonFaces[i])
            testingLabels.append(labelVectorNonFaces[i])
    return trainingData, trainingLabels, testingData, testingLabels

def differentSplitData():
    trainingData = []
    testingData = []
    trainingLabels = []
    testingLabels = []
    for i in range(0, len(dataMatrix), 10):  # Jump by 10 each iteration
        for j in range(10):
            ind = i + j
            if j < 7:
                trainingData.append(dataMatrix[ind])
                trainingLabels.append(labelVector[ind])
            else:
                testingData.append(dataMatrix[ind])
                testingLabels.append(labelVector[ind])
    return trainingData, trainingLabels, testingData, testingLabels