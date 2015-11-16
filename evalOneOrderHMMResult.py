#-*-coding:utf-8-*-
__author__ = 'Administrator'
import string
fr = open("E:\\PyProj\\Others\\9-1\\rite_HMM_data _test_result_BWL_1.txt")
sentence = fr.readline()
pos = fr.readline()
event = fr.readline().strip()
pred = fr.readline().strip()
cntEvent = 0
cntPred = 0
cntRight = 0
while(sentence):
    events = event.split(" ")
    preds = pred.split(" ")
    le = len(events)
    for i in range(le):
        m = string.atoi(events[i])
        if(m!=7):
            cntEvent += 1
        n = string.atoi(preds[i])
        if(n!=7):
            cntPred += 1
        if(m == n and m!=7):
            cntRight += 1
    sentence = fr.readline()
    pos = fr.readline()
    event = fr.readline().strip()
    pred = fr.readline().strip()
fr.close()
print "events:"+str(cntEvent)
print "preds:"+str(cntPred)
print "rights:"+str(cntRight)