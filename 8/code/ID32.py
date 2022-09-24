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

class TreeNode:
    def __init__(self, ids=None, children=[], entropy=0, depth=0,arrAttr=None):
        self.ids = ids           # index of data in this node
        self.entropy = entropy   # entropy, will fill later
        self.depth = depth       # distance to root node
        self.split_attribute = None  # which attribute is chosen, it non-leaf
        self.children = children  # list of its child nodes
        self.order = None       # order of values of split_attribute in children
        self.label = None       # label of node if it is a leaf #Rd NotRd
        self.remainAttr=arrAttr
    def set_properties(self, split_attribute, order):
        self.split_attribute = split_attribute
        self.order = order
    def set_threshold(self, _threshold):
        self.threshold=_threshold
    def set_label(self, label):
        self.label = label

def entropy(freq): # 
    freq_0 = freq[np.array(freq).nonzero()[0]]
    prob_0 = freq_0/float(freq_0.sum())
    rsEntrophy = -np.sum(prob_0*np.log2(prob_0)) 
    return rsEntrophy
class ID3:

    """Creates a decision tree with C4.5 algorithm"""

    def __init__(self):
        self.classes = []  # {play,dont play}
        self.arrValue = {}
        self.numAttributes = -1
        self.arrAttr = []
        self.tree = None
        self.max_depth=10
        self.min_gain=1e-4
        self.min_samples_split=2
    def newTest(self,data,target):
        with open("dataTest", 'wb') as f:
            pickle.dump(data, f)
        with open("targetTest", 'wb') as f:
            pickle.dump(target, f)
    def newData(self,data,target):
        with open("data", 'wb') as f:
            pickle.dump(data, f)
        with open("target", 'wb') as f:
            pickle.dump(target, f)
    def layDuLieu2(self):
        quadRangle= Quadrangle()
        self.arrAttr=list(self.data)
        for attr in self.arrAttr:
            self.arrValue[attr]='continuous' # outlook overcast rain sunny 
        self.arrValue["Quadrangle"] = quadRangle.getQuad() # 0,1,2,3,4,5
       
        
        
    def printNode(self, node, indent=""):
        if  node.children:
            if node.threshold is None:
                for index, child in enumerate(node.children):
                    if not child.children and child != None :  # true
                        print(indent + node.split_attribute + " = " +
                              node.order[index] + " : " + str(child.label)+"\t")
                    else:
                        print(indent + node.split_attribute + " = " +
                              node.order[index] + " : ")
                        self.printNode(child, indent + "\t|")
            else:
                leftChild = node.children[0]
                rightChild = node.children[1]
                if not leftChild.children:
                    print(indent + node.split_attribute + " < " +
                          str(node.threshold) + " : " + leftChild.label+"\t")
                else:
                    print(indent + node.split_attribute + " < " +
                          str(node.threshold)+" : ")
                    self.printNode(leftChild, indent + "\t|")
                if not rightChild.children:
                    print(indent + node.split_attribute + " > " +
                          str(node.threshold) + " : " + rightChild.label+"\t")
                else:
                    print(indent + node.split_attribute + " > " +
                          str(node.threshold) + " : ")
                    self.printNode(rightChild, indent + "\t|")
       
    def _predict(self,dataT,targetT):
        npoints = dataT.count()[0]  # wind :14
        labels = [None]*npoints  # [none,none,none....none] :14
        for n in range(npoints):  # 0-13
            x = dataT.iloc[n, :]  # sunny hot high weak
            node = self.root
            while node.children:
                # order [sunny,overcast,rainy]  # split_attribute 'outlook'
                if(self.arrValue[node.split_attribute]=='continuous'):
                    if(x[node.split_attribute]<node.threshold):
                        node = node.children[0]
                    else:
                        node = node.children[1]
                else:
                    node=node.children[node.order.index(x[node.split_attribute])]
            labels[n] = node.label


        tp=len([i for i, j in zip(labels, targetT) if i == j and i=='Rd'])
        tn=len([i for i, j in zip(labels, targetT) if i == j and i=='Not Rd'])
        fn=len([i for i, j in zip(labels, targetT) if i=='Not Rd' and j=='Rd'])
        fp=len([i for i, j in zip(labels, targetT) if i=='Rd' and j=='Not Rd'])
        recall=tp/(tp+fn)
        precision =0 
        if(tp+fp!=0):
            precision=tp/(tp+fp)
        acc=((tp+tn)*100/len(targetT))
        print("\n===========confuse Matrix:============")
        print("\tNot Rd\tRd")
        print("Not Rd\t"+str(tn/(tn+fp))+"\t"+str(fp/(tn+fp)))
        print("Rd\t"+str(fn/(tp+fn))+"\t"+str(tp/(tp+fn)))

        
        print("recall\t"+str(recall))
        print("precision\t"+str(precision))
        print("accuracy(%):"+str(acc))
        return labels    

    def fit(self):
        self.Ntrain = self.data.count()[0]  # 14
        ids = range(self.Ntrain)  # range(0 14) (0 <1000)
        self.root = TreeNode(ids=ids, entropy=self._entropy(
            ids), depth=0,arrAttr=self.arrAttr)  # entropy=0.9402859586706311
        queue = [self.root]  # len=1 [1,2,3,46,"str",Tree]
        while(queue):
            node = queue.pop()
            if self._isSameClass(node) or len(node.remainAttr)==0 :
                self._set_label(node)
                continue
            if node.depth < self.max_depth or node.entropy < self.min_gain:  # min_gain=0.0001
                node.children = self._split(node)
                if not node.children:  # leaf node node.children=[]
                    self._set_label(node)
                else:
                    queue += node.children
            else:
                self._set_label(node)


    def _isSameClass(self,node):
        ids=node.ids
        if(len(ids)==0):
            return False
        freq = list(itemgetter(*ids)(self.target))
        freq = pd.Series(freq)
        freq= freq.value_counts()
        if(len(freq)==1):
            return True
        else:
            return False
    def _getLabel(self,node):
        ids=node.ids
        if(len(ids)==0):
            return 'Khong co du lieu'
        freq = list(itemgetter(*ids)(self.target))
        freq = pd.Series(freq)
        freq= freq.value_counts()
        if(len(freq)==1):
            return freq.keys()[0]
        elif(len(freq)==2):
            tile=freq[0]/(freq[1]+freq[0])
            if( freq.keys()[0]=='Not Rd' and tile>0.5):
                return 'Not Rd'
            else:
                return 'Rd'
                
            

        
    def _set_label(self, node):
        ids=node.ids
        node.set_label(self._getLabel(node))
       
    def _entropy(self, ids):
        if len(ids) <= 0:
            return 0
        freq = list(itemgetter(*ids)(self.target))
        freq = pd.Series(freq)
        freq = freq.value_counts()
        return entropy(freq)  
    
    def _split(self, node):
        ids = node.ids
        best_gain = 0
        bSub_ids = []
        best_attribute = None #outlook
        order = None
        bThreshold=None
        sub_data = self.data.iloc[ids, :]  # ids range(0,14)
            
        # ['outlook', 'temperature', 'humidity', 'wind']
        for i, att in enumerate(node.remainAttr):
            # ['sunny','overcast','rainy']
            if(self.arrValue[att]!='continuous'):
                values = self.arrValue[att]
                splits = []
                for val in values:  # val= sunny
                    sub_ids = sub_data.index[sub_data[att]
                                         == val].tolist()  # [0, 1, 7, 8, 10]
                    splits.append([sub_id for sub_id in sub_ids])
                # information gain
                HxS=0
                for split in splits:
                    HxS+=len(split)*self._entropy(split) / len(ids)
                gain = node.entropy - HxS  # 0.9402859586706311-0.6935361388961919=0.24674981977443922
               
                if gain > best_gain:
                    best_gain = gain
                    bSub_ids = splits
                    best_attribute = att
                    order = values
            elif(self.arrValue[att]=='continuous'):
                sub_data=sub_data.sort_values(att)
                subdataTemp=sub_data[att].values.tolist()
                for j in range (0,len(sub_data)-1):
                    if(subdataTemp[j]!=subdataTemp[j+1]):
                        splits=[]
                        threshold=(subdataTemp[j]+subdataTemp[j+1])/2
                        less = sub_data.index[sub_data[att]<threshold].tolist()
                        greater = sub_data.index[sub_data[att]>threshold].tolist()
                        splits.append(less)
                        splits.append(greater)
                        if min(map(len, splits)) < self.min_samples_split:
                            continue
                        # information gain
                        HxS = 0
                        for split in splits:
                            HxS += len(split)*self._entropy(split) / len(ids)  # 0.6935361388961919
                        gain = node.entropy - HxS  # 0.9402859586706311-0.6935361388961919=0.24674981977443922
                        if gain > best_gain:
                            bThreshold=threshold
                            best_gain = gain
                            bSub_ids = splits
                            best_attribute = att
                            order = []
        remainAttr=node.remainAttr
      
        if(best_attribute=='Quadrangle'):
            remainAttr.remove(best_attribute)
        node.set_properties(best_attribute, order)
        node.set_threshold(bThreshold)
        child_nodes = [TreeNode(ids=split,
                                entropy=self._entropy(split), depth=node.depth + 1,arrAttr=remainAttr) for split in bSub_ids]
        return child_nodes  
     

 
