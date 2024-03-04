# Ignore this if we use the .ipynb file

import numpy as np
import scipy as sp
from sklearn.metrics import accuracy_score
from sklearn.neighbors import KNeighborsClassifier

def LDA(trainingData, trainingLabels, testingData, testingLabels):
    matrix = np.array(trainingData)
    # Split the training data into 40 classes
    classMatrices = np.split(matrix, indices_or_sections=40)

    # Compute class means
    classMeans = np.mean(classMatrices, axis=1)
    
    # Compute the overall sample mean
    overallMean = np.mean(matrix, axis=0)

    # Compute the between-class scatter matrix
    Sb = getBetweenClass(classMeans, overallMean)
    print("between: ", Sb)

    # Centering each class
    centeredClassMatrices = getCenteredClasses(classMatrices, classMeans)

    # Compute the within-class scatter matrix
    S = getWihinClass(overallMean, centeredClassMatrices)
    print("within: ", S)
    
    # Check if S is singular
    isSingular = np.linalg.det(S) == 0
    if isSingular:
        print("S is singular")
    else:
        print("S is not singular")

    # Computing the inverse of S
    print("Computing S inverse")
    SInverse = sp.linalg.pinv(S)

    # Computing the S inverse * Sb matrix
    print("Computing S inverse * Sb")
    SInv_Sb = np.dot(SInverse, Sb)

    # Computing eigenvalues and vectors
    print("Computing eigenvalues and vectors")
    eigenValues, eigenVectors = np.linalg.eig(SInv_Sb)
    print("eigenvectors: ", eigenVectors)

    # Sorting to find dominant vectors
    sortedIndecies = np.argsort(eigenValues)[::-1]
    sortedEigenVectors = eigenVectors[:,sortedIndecies]
    U = np.real(sortedEigenVectors[:,:39])
    print("projection matr: ", U)

    # Projecting data
    print("Projecting")
    projectedTrainingData = np.dot(trainingData , U)
    projectedTestingData = np.dot(testingData , U)

    # Classification
    print("Classifying")
    classifier = KNeighborsClassifier(1)
    classifier.fit(projectedTrainingData, trainingLabels)
    prediction = classifier.predict(projectedTestingData)
    accuracy = accuracy_score(testingLabels, prediction)

    print ("Accuracy = ", accuracy * 100)
    print("Done")    


def getBetweenClass(classMeans, overallMean):
    print("Computing Sb")
    Sb = np.zeros((len(overallMean), len(overallMean)))
    for classMean in classMeans:
        sub = classMean - overallMean
        mul = np.outer(sub, sub)
        Sb += 5 * mul
    return Sb


def getCenteredClasses(classMatrices, classMeans):
    centeredClassMatrices = []
    print("Computing centered matrices")
    for classMatrix, classMean in zip(classMatrices, classMeans):
        centeredClass = []
        for row in classMatrix:
            centeredClass.append(row - classMean)
        centeredClassMatrices.append(centeredClass)
    return centeredClassMatrices


def getWihinClass(overallMean, centeredClassMatrices):
    print("Computing S")
    S = np.zeros((len(overallMean), len(overallMean)))
    for centeredClass in centeredClassMatrices:
        centeredClassMat = np.array(centeredClass)
        S += np.dot(np.transpose(centeredClassMat), centeredClassMat)
    return S