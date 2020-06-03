#importing important libraries
#import pymongo
import pickle
import time
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn import svm

DB_URL = 'mongodb://usr1:password@localhost:27017/?authSource=paymentsdb'
DB = 'paymentsdb'
COLLECTION_NAME  = 'TrainedModel'

def saveTrainedModelJson(jsonModel,name):
    return saveTrainedModel(jsonModel['model'],jsonModel['modelRefData'],jsonModel['scalar'],jsonModel['pca'],name)
	
def checkTransaction(modelFor, arr):
    jsonData = loadTrainedModelDetails(modelFor)
    if(jsonData is None):
        return -999
    scalar = pickle.loads(jsonData['scalar'])
    pca = pickle.loads(jsonData['pca'])
    model = pickle.loads(jsonData['model'])
    record = scalar.transform(arr)
    record = pca.transform(record)
    prediction = model.predict(record)
    return prediction

# Trains the n dimensional data provided to this function and returns json structure of learned model
def trainData(ndArray):
    scalar = StandardScaler().fit(ndArray)
    scaledData = scalar.transform(ndArray)
    pcaAnalyzer = PCA(n_components=2).fit(scaledData)
    pcaAnalyzedData = pcaAnalyzer.transform(scaledData)
    clf = svm.OneClassSVM(nu=0.1, kernel="rbf", gamma=0.1)
    clf.fit(pcaAnalyzedData)
    trainedModelObj = {'model':clf,'modelRefData':pcaAnalyzedData,'scalar':scalar,'pca':pcaAnalyzer}
    return trainedModelObj

def checkprint(msg):
    print('welcome to my library '+msg)
    
    
