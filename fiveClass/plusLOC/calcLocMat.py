#-*-coding:utf-8-*-
__author__ = 'Administrator'
import string
N = 7
LocMat = [([0] * 11) for i in range(N)]
fresult = open("E:\\PyProj\\Others\\7-3\\LOC\\rite_HMM_data.txt")
sentence = fresult.readline().strip()
loc = fresult.readline().strip()
event = fresult.readline().strip()
while(sentence):
    events = event.split(" ")
    locs = loc.split(" ")
    l = len(events)
    for i in range(l):
        m = string.atoi(events[i])
        n = string.atoi(locs[i])
        LocMat[m][n] += 1
    sentence = fresult.readline().strip()
    loc = fresult.readline().strip()
    event = fresult.readline().strip()
fresult.close()
for i in range(N):
    print LocMat[i]