#-*- coding:utf-8 -*-
__author__ = 'Administrator'
import string
N = 7
TF = [([0] * 40) for i in range(N)]
ftrain = open("E:\\PyProj\\Others\\7-3\\rite_HMM_data _test_result_tri_gram.txt")
sentence = ftrain.readline()
pos = ftrain.readline()
anoEvent = ftrain.readline().strip()
event = ftrain.readline().strip()
while(sentence):
    events = event.split(" ")
    last = string.atoi(events[0])
    l = len(events)
    cnt = 1
    for i in range(1,l):
        curr = string.atoi(events[i])
        if(curr == last):
            cnt += 1
        else:
            TF[last][cnt] += 1
            cnt = 1
        last = curr
    sentence = ftrain.readline()
    pos = ftrain.readline()
    anoEvent = ftrain.readline().strip()
    event = ftrain.readline().strip()
ftrain.close()
for i in range(N):
    l = 0
    c = 0
    for j in range(2,39):
        l += j*TF[i][j]
        c += TF[i][j]
    print l*1.0/c," ",TF[i]

