# -*-coding:utf-8-*-
__author__ = 'Administrator'
import string

N = 7
fr = open("E:\\PyProj\\Others\\7-3\\LOC\\rite_HMM_data _test_result_tri_gram.txt")
#rules filter
def rulesFilter(path,poss,preds,errTag,rightTag):
    #read rules
    rules = [([0] * 5) for i in range(360)]
    frules = open(path)
    line = frules.readline().strip()
    rulesIdx = 0
    while (line):
        tags = line.split(" ")
        rules[rulesIdx][0] = string.atoi(tags[0])
        rules[rulesIdx][1] = string.atoi(tags[1])
        rules[rulesIdx][2] = string.atoi(tags[2])
        rules[rulesIdx][3] = string.atoi(tags[3])
        rules[rulesIdx][4] = string.atoi(tags[4])
        rulesIdx += 1
        line = frules.readline().strip()
    frules.close()
    #filter
    for i in range(2,len(preds)-2):
        if(preds[i] == errTag):
            for j in range(rulesIdx):
                b = 1
                for k in range(5):
                    if(string.atoi(poss[i+k-2]) != rules[j][k]):
                        b = 0
                        break
                if(b == 1):
                    preds[i] = rightTag
                    break
    return preds
#===============================================================================
sentence = fr.readline().strip()
pos = fr.readline().strip()
event = fr.readline().strip()
pred = fr.readline().strip()
while (sentence):
    words = sentence.split(" ")
    poss = pos.split(" ")
    preds = pred.split(" ")
    l = len(poss)
    print sentence
    print pos
    print event
    path = "E:\\PyProj\\Others\\7-3\\LOC\\rulesK2L.txt"
    preds = rulesFilter(path,poss,preds,"2","4")
    path = "E:\\PyProj\\Others\\7-3\\LOC\\rulesZ2L.txt"
    preds = rulesFilter(path,poss,preds,"0","4")
    path = "E:\\PyProj\\Others\\7-3\\LOC\\rulesK2T.txt"
    preds = rulesFilter(path,poss,preds,"2","3")
    path = "E:\\PyProj\\Others\\7-3\\LOC\\rulesZ2T.txt"
    preds = rulesFilter(path,poss,preds,"0","3")
    path = "E:\\PyProj\\Others\\7-3\\LOC\\rulesK2W.txt"
    preds = rulesFilter(path,poss,preds,"2","1")
    path = "E:\\PyProj\\Others\\7-3\\LOC\\rulesZ2W.txt"
    preds = rulesFilter(path,poss,preds,"0","1")
    path = "E:\\PyProj\\Others\\7-3\\LOC\\rulesK2Z.txt"
    preds = rulesFilter(path,poss,preds,"2","0")
    path = "E:\\PyProj\\Others\\7-3\\LOC\\rulesZ2K.txt"
    preds = rulesFilter(path,poss,preds,"0","2")
    path = "E:\\PyProj\\Others\\7-3\\LOC\\rulesK2F.txt"
    preds = rulesFilter(path,poss,preds,"2","5")
    path = "E:\\PyProj\\Others\\7-3\\LOC\\rulesZ2F.txt"
    preds = rulesFilter(path,poss,preds,"0","5")
    path = "E:\\PyProj\\Others\\7-3\\LOC\\rulesK2RA.txt"
    preds = rulesFilter(path,poss,preds,"2","6")
    path = "E:\\PyProj\\Others\\7-3\\LOC\\rulesZ2RA.txt"
    preds = rulesFilter(path,poss,preds,"0","6")
    path = "E:\\PyProj\\Others\\7-3\\LOC\\rulesN2K.txt"
    preds = rulesFilter(path,poss,preds,"5","2")
    for i in preds:
        print i.strip(),
    print "\n",

    sentence = fr.readline().strip()
    pos = fr.readline().strip()
    event = fr.readline().strip()
    pred = fr.readline().strip()
fr.close()
