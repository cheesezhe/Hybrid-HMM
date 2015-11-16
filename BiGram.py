# -*-coding:utf-8-*-
__author__ = 'Administrator'
import string
N = 16
M = 24
A = [([0.0] * N) for i in range(N)]
B = [([0.0] * M) for i in range(N)]
PI = [0.0 for i in range(N)]
#统计次数
fr = open("E:\\PyProj\\Others\\9-1\\rite_HMM_data_train.txt")
sentence = fr.readline()
pos = fr.readline()  # observations
event = fr.readline()  # states
while (sentence):
    poss = pos.strip().split(' ')
    events = event.strip().split(' ')
    lp = len(poss)
    le = len(events)
    if (lp != le):
        print sentence
    length = lp
    PI[string.atoi(events[0])] += 1
    for i in range(length - 1):
        A[string.atoi(events[i])][string.atoi(events[i + 1])] += 1
    for i in range(length):
        B[string.atoi(events[i])][string.atoi(poss[i])] += 1
    sentence = fr.readline()
    pos = fr.readline()  # observations
    event = fr.readline()  # states
fr.close()
#计算概率
#A=N*N,B=N*M,PI=1*N
for i in range(N):
    s = sum(A[i])
    for j in range(N):
        A[i][j] /= s
for i in range(N):
    s = sum(B[i])
    for j in range(M):
        B[i][j]/=s
s = sum(PI)
for i in range(N):
    PI[i] /= s
for i in range(N):
    print 'State'
    print 'Pi ',PI[i]
    print 'A',
    for j in range(N):
        print ' '+str(A[i][j]),
    print '\nIntegerOPDF [',
    for j in range(M):
        print ' '+str(B[i][j]),
    print ' ]\n'