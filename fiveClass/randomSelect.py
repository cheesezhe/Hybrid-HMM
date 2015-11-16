#-*-coding:utf-8-*-
__author__ = 'Administrator'
import random
cntTest = 810
testSet = set()
trainSet = set()
fdata = open("E:\\PyProj\\Others\\7-3\\rite_HMM_data.txt")
ftest = open("E:\\PyProj\\Others\\7-3\\rite_HMM_data_test.txt",'w')
ftrain = open("E:\\PyProj\\Others\\7-3\\rite_HMM_data_train.txt",'w')
wordList = []
posList = []
eventList = []
word = fdata.readline()
pos = fdata.readline()
event = fdata.readline()
while(word):
    wordList.append(word)
    posList.append(pos)
    eventList.append(event)
    word = fdata.readline()
    pos = fdata.readline()
    event = fdata.readline()
while(len(testSet)<=cntTest):
    idx = random.randint(0,len(wordList))
    testSet.add(idx)
for i in range(len(wordList)):
    if i in testSet:
        ftest.write(wordList[i].strip()+'\n')
        ftest.write(posList[i].strip()+'\n')
        ftest.write(eventList[i].strip()+'\n')
    else:
        ftrain.write(wordList[i].strip()+'\n')
        ftrain.write(posList[i].strip()+'\n')
        ftrain.write(eventList[i].strip()+'\n')
fdata.close()
ftest.close()
ftrain.close()
