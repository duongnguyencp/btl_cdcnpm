import math
from Quadrangle import Quadrangle
import numpy as np
import pandas as pd
import pydotplus
import pickle
from sklearn.model_selection import train_test_split
from sklearn import tree
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.preprocessing import LabelEncoder
import matplotlib.image
import matplotlib.pyplot
from operator import itemgetter
from Quadrangle import Quadrangle
from ID32 import ID3
import joblib
def newDataPart(listPart):
    with open("listPart7", 'wb') as f:
        pickle.dump(listPart, f)
def predictAllModel():  
    listModel=joblib.load('savemodel7.pkl')
    listPart=[]
    with open ("listPart",'rb') as f:
        listPart=pickle.load(f)
    for part in listPart:
        dataT=part[0]
        targetT=part[1]
        c1=listModel.pop()
        c1._predict(dataT,targetT)
def createModelCrossValidation():
    listPart=[]
    with open ("listPart6",'rb') as f:
        listPart=pickle.load(f)
    listModel=[]
    for i in range(0,len(listPart)):
        c1=ID3()
        listPart2=[]
        listPart2=listPart.copy()
        del listPart2[i]
        tempData=listPart2[0][0]
        tempTarget=listPart2[0][1]
        for j in range(1,len(listPart2)):
            tempData2=tempData
            tempData=tempData2.append(listPart2[j][0])
            tempTarget.extend(listPart2[j][1])
        data=tempData
        target=tempTarget
        data = data.reset_index(drop=True)
        c1.data=data
        c1.target=target
        c1.layDuLieu2()
        c1.fit()
        c1.printNode(c1.root)
        listModel.append(c1)
    joblib.dump(listModel,'savemodel5Full.pkl')


def splitData(dataSize,numberFolds):
    df = pd.read_csv('mar.csv')
    unit=int(dataSize/numberFolds)
    startDt=0
    endDt=0
    startT=0
    endT=0
    listPart=[]
    for i in range(1,numberFolds+1):
        part=[]
        start=(i-1)*unit
        end=start+unit
        data = df.iloc[start:end, [5,-1]]
        target = df.iloc[start:end, 6]
        dataLO=df.iloc[start:end,3]
        dataLA=df.iloc[start:end,2]
        quadRangle= Quadrangle()
        data.insert(0,'Quadrangle','tao cot')
        nRows = data.count()[0]
        target=['Rd' if 'Rd' in target.iloc[i] else 'Not Rd' for i in range(nRows)]
        q=[quadRangle.toQuad(dataLA.iloc[i],dataLO.iloc[i]) for i in range(nRows)]
        data['Quadrangle']=q
        listPart.append([data,target])
    newDataPart(listPart)

def buildModel():
    splitData(384343,7)
    #createModelCrossValidation()

#main
buildModel()   
# predictAllModel()



