#-*-coding:utf-8-*-
__author__ = 'Administrator'
import string
fr = open("E:\\PyProj\\Others\\rite_HMM_data _test_result_HMM.txt")
sentence = fr.readline()
pos = fr.readline()
event = fr.readline().strip()
pred = fr.readline().strip()
cntEvent = [0 for i in range(16)]
cntPred = [0 for i in range(16)]
cntRight = [0 for i in range(16)]
while(sentence):
    events = event.split(" ")
    preds = pred.split(" ")
    le = len(events)
    for i in range(le):
        m = string.atoi(events[i])
        cntEvent[m] += 1
        n = string.atoi(preds[i])
        cntPred[n] += 1
        if(m == n):
            cntRight[m] += 1
    sentence = fr.readline()
    pos = fr.readline()
    event = fr.readline().strip()
    pred = fr.readline().strip()
fr.close()
print "events:"+str(cntEvent)+str(sum(cntEvent))
print "preds:"+str(cntPred)+str(sum(cntPred))
print "rights:"+str(cntRight)+str(sum(cntRight))