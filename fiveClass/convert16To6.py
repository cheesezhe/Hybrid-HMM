#-*-coding:utf-8-*-
__author__ = 'Administrator'
fdata = open("E:\\PyProj\\Others\\7-3\\rite_HMM_data.txt")
fdata2 = open("E:\\PyProj\\Others\\7-3\\rite_HMM_data2.txt",'w')
sentence = fdata.readline()
pos = fdata.readline()
event = fdata.readline()
while(sentence):
    events = event.strip().split(' ')
    l = len(events)
    for i in range(l):
        if(events[i] == "1"):
            events[i] = "5"
        elif(events[i] == "3"):
            events[i] = "2"
        elif(events[i] == "4"):
            events[i] = "5"
        elif(events[i] == "6"):
            events[i] = "4"
        elif(events[i] == "7"):
            events[i] = "5"
        elif(events[i] == "8"):
            events[i] = "2"
        elif(events[i] == "9"):
            events[i] = "6"
        elif(events[i] == "10"):
            events[i] = "0"
        elif(events[i] == "11"):
            events[i] = "5"
        elif(events[i] == "12"):
            events[i] = "5"
        elif(events[i] == "13"):
            events[i] = "0"
        elif(events[i] == "14"):
            events[i] = "1"
        elif(events[i] == "15"):
            events[i] = "3"
    fdata2.write(sentence)
    fdata2.write(pos)
    for i in events:
        fdata2.write(i+" ")
    fdata2.write("\n")
    sentence = fdata.readline()
    pos = fdata.readline()
    event = fdata.readline()
fdata2.close()
fdata.close()