#-*-coding:utf-8-*-
__author__ = 'Administrator'
import string
N = 7
fr = open("E:\\PyProj\\Others\\7-3\\rite_HMM_data _test_result_bi_gram.txt")
sentence = fr.readline()
pos = fr.readline()
event = fr.readline().strip()
pred = fr.readline().strip()
cntEvent = [0 for i in range(N)]
cntPred = [0 for i in range(N)]
cntRight = [0 for i in range(N)]
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
# print "events:"+str(cntEvent)
# print "preds:"+str(cntPred)
# print "rights:"+str(cntRight)
print str(cntEvent)
print str(cntPred)
print str(cntRight)