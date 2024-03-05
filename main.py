# Ignore this if we use the .ipynb file

import DatasetSplitter as ds
from LDA import LDA

trainingData, trainingLabels, testingData, testingLabels = ds.splitData2()

LDA(trainingData, trainingLabels, testingData, testingLabels)
