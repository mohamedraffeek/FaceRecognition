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