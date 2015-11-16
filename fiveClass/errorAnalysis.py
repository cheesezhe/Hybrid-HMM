#-*-coding:utf-8-*-
__author__ = 'Administrator'
import string
N = 7
ErrMat = [([0] * N) for i in range(N)]
fresult = open("E:\\PyProj\\Others\\7-3\\LOC\\rite_HMM_data _test_result_tri_gram.txt")
sentence = fresult.readline().strip()
pos = fresult.readline().strip()
event = fresult.readline().strip()
result = fresult.readline().strip()
while(sentence):
    words = sentence.split(" ")
    poss = pos.split(" ")
    events = event.split(" ")
    results = result.split(" ")
    l = len(events)
    for i in range(l):
        m = string.atoi(events[i])
        n = string.atoi(results[i])
        ErrMat[m][n] += 1
        if(i>=2 and i<l-2 and m == 2 and n == 5):
            print poss[i-2]+" "+poss[i-1]+" "+poss[i]+" "+poss[i+1]+" "+poss[i+2]
    sentence = fresult.readline().strip()
    pos = fresult.readline().strip()
    event = fresult.readline().strip()
    result = fresult.readline().strip()
fresult.close()
# for i in range(N):
#     print ErrMat[i]