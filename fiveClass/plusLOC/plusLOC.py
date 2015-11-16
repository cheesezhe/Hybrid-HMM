#-*-coding:utf-8-*-
__author__ = 'Administrator'
fdata = open("E:\\PyProj\\Others\\7-3\\LOC\\rite_HMM_data.txt")
fdata2 = open("E:\\PyProj\\Others\\7-3\\LOC\\rite_HMM_data2.txt",'w')
sentence = fdata.readline()
pos = fdata.readline()
event = fdata.readline()
while(sentence):
    poss = pos.strip().split(' ')
    l = len(poss)
    pos = ""
    #TODO:
    for i in range(1,l+1):
        pos += str(i*10/l)+" "
    pos += "\n"

    fdata2.write(sentence)
    fdata2.write(pos)
    fdata2.write(event)

    sentence = fdata.readline()
    pos = fdata.readline()
    event = fdata.readline()
fdata2.close()
fdata.close()