import numpy as np

def execute(D):
    matrix = np.array(D)
    classMatrices = np.split(matrix, 40)
    classMeans = []
    for classMatrix in classMatrices:
        classMeans.append(np.mean(classMatrix, 0))
    overallMean = np.mean(matrix, 0)
    Sb = [[0 for x in range(len(overallMean))] for y in range(len(overallMean))]
    for classMean in classMeans:
        sub = np.subtract(classMean, overallMean)
        mul = np.outer(sub, sub)
        Sb = np.add(Sb, 5 * mul)
    
