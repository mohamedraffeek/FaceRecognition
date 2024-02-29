import DatasetGenerator

dataMatrix, labelVector = DatasetGenerator.generateData()

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