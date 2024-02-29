import DatasetSplitter as ds
import LDA

trainingData, trainingLabels, testingData, testingLabels = ds.splitData()

LDA.execute(trainingData)
