# -*-coding:utf-8-*-
__author__ = 'Administrator'
import string
import math
# 通过训练数据集得到3元模型初始数据
ftrain = open("E:\\PyProj\\Others\\7-3\\rite_HMM_data_train.txt")
N = 7
M = 24
A0 = [([1.0e-20] * N) for i in range(N)]
A = [[([1.0e-20] * N) for i in range(N)] for j in range(N)]
B0 = [([1.0e-20] * M) for i in range(N)]
B = [[([1.0e-20] * M) for i in range(N)] for j in range(N)]
PI0 = [1.0e-20 for i in range(N)]
ftrain.readline()  #filter word seqs
pos = ftrain.readline()
event = ftrain.readline()
while (pos):
    poss = pos.strip().split(' ')
    events = event.strip().split(' ')
    l = len(poss)
    PI0[string.atoi(events[0])] += 1
    B0[string.atoi(events[0])][string.atoi(poss[0])] += 1
    A0[string.atoi(events[0])][string.atoi(events[1])] += 1
    for i in range(l - 2):
        A[string.atoi(events[i])][string.atoi(events[i + 1])][string.atoi(events[i + 2])] += 1
    for i in range(l - 1):
        B[string.atoi(events[i])][string.atoi(events[i + 1])][string.atoi(poss[i + 1])] += 1
    ftrain.readline()
    pos = ftrain.readline()
    event = ftrain.readline()
sP0 = sum(PI0)
for i in range(N):
    PI0[i] /= sP0
    #print "PI0 ",PI0[i]
    sP = 0
    sA0 = 0
    for j in range(N):
        sA0 += A0[i][j]
    #for j in range(N):
        #sP += PI[i][j]
    for j in range(N):
        A0[i][j] /= sA0
        #print "A0 ",A0[i][j]
        #PI[i][j] /= sP
        sA = 0
        sB = 0
        for k in range(N):
            sA += (A[i][j][k])
        for k in range(M):
            sB += (B[i][j][k])
        for k in range(N):
            A[i][j][k] /= sA
            #print "A ",A[i][j][k]
        for k in range(M):
            #print "B",B[i][j][k]," sB ",sB,
            B[i][j][k] /= sB
            #print " B ",B[i][j][k]
    sB0 = 0
    for j in range(M):
        sB0 += (B0[i][j])
    for j in range(M):
        B0[i][j] /= sB0
        #print "B0 ",B0[i][j]
ftrain.close()
#TODO:与3元模型对应的Viterbi算法
def triGramViterbi(N, M, A, B0, B, PI0, observed):  #observed 是数字序列,且长度最短为3
    sta = []
    LEN = len(observed)
    if (LEN < 3):
        return "Too Short Input Text."

    Delta0 = [([-1000.0] * N) for i in range(2)]
    Delta = [[([-1000.0] * N) for i in range(N)] for j in range(LEN)]
    path = [([0] * N) for i in range(LEN)]
    #path = [([([([0]*N) for i in range(N)])for j in range(LEN)])]
    #第1天计算，状态的初始概率*隐藏状态到观察状态的条件概率
    for i in range(N):
        Delta0[0][i] = math.log10(PI0[i]) + math.log10(B0[i][observed[0]])
        path[0][i] = -1
    #第2天计算，状态的初始概率*隐藏状态到观察状态的条件概率
    for j in range(N):  #跳转状态
        max = -1000.0
        idx = 0
        for i in range(N):
            if (Delta0[0][i] +math.log10(A0[i][j])  > max):
                max = Delta0[0][i] + math.log10(A0[i][j])
                idx = i
        xxx = max + math.log10(B[idx][j][observed[1]])
        Delta[1][idx][j] = xxx
        path[1][j] = idx
    # 第2天以后的计算
    # 前一天的每个状态转移到当前状态的概率最大值
    # *
    # 隐藏状态到观察状态的条件概率
    for t in range(2, LEN):  #时间t
        for k in range(N):  #跳转状态
            max = -1000.0
            idx = 0
            for i in range(N):
                for j in range(N):
                    if (Delta[t - 1][i][j] +math.log10(A[i][j][k])  > max):
                        max = (Delta[t - 1][i][j]) +math.log10(A[i][j][k])
                        idx = j
            Delta[t][idx][k] = max +math.log10(B[idx][k][observed[t]])
            path[t][k] = idx
    #找到最大输出序列
    max = -1000.0
    idx = 0
    lidx = 0
    for i in range(N):
        for j in range(N):
            if (Delta[LEN - 1][i][j] > max):
                max = Delta[LEN - 1][i][j]
                lidx = j
                idx = i
    sta.append(lidx)
    sta.append(idx)
    for i in range(LEN - 2, 0, -1):
        idx = path[i][idx]
        sta.append(idx)
    sta.reverse()
    return sta


ftest = open("E:\\PyProj\\Others\\7-3\\rite_HMM_data_test.txt")
word = ftest.readline()
pos = ftest.readline()
event = ftest.readline()
while (word):
    poss = pos.strip().split(' ')
    observed = []
    for i in poss:
        observed.append(string.atoi(i))
    print word,
    print pos,
    print event,
    sta = triGramViterbi(N, M, A, B0, B, PI0, observed)
    for i in sta:
        print str(i),
    print ' '
    word = ftest.readline()
    pos = ftest.readline()
    event = ftest.readline()
