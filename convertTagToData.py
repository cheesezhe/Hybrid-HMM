#-*-coding:utf-8-*-
__author__ = 'Administrator'
eventTag = ['A', 'Ma', 'D', 'P', 'Ai', 'M', 'L', 'O', 'Re', 'Ra', 'Th', 'I', 'Rn', 'Cau', 'EP', 'T']
posTag =['nh', 'ni', 'nl', 'nd', 'nz', 'ns', 'nt', 'ws', 'wp', 'a', 'c', 'b', 'd', 'i', 'h', 'j', 'm', 'n', 'q', 'p', 'r', 'u', 'v', 'z']
fr = open("E:\\PyProj\\Others\\rite_3list.txt")
fw = open("E:\\PyProj\\Others\\rite_HMM_data.txt",'w')
sentence = fr.readline()
pos = fr.readline()
event = fr.readline()
while(pos):
    pos_data = []
    event_data = []
    poss = pos.rstrip().split(" ")
    events = event.rstrip().split(" ")
    for i in poss:
        pos_data.append(posTag.index(i))
    for i in events:
        event_data.append(eventTag.index(i))
    fw.write(sentence)
    for i in pos_data:
        fw.write(str(i)+' ')
    fw.write('\n')
    for i in event_data:
        fw.write(str(i)+' ')
    fw.write('\n')
    sentence = fr.readline()
    pos = fr.readline()
    event = fr.readline()

fw.close()
fr.close()