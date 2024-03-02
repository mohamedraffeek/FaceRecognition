import DatasetSplitter as ds
from LDA import LDA

trainingData, trainingLabels, testingData, testingLabels = ds.splitData()

LDA(trainingData, trainingLabels, testingData, testingLabels)
