#-*-coding:utf-8-*-
__author__ = 'ZhangHe'
fpos = open("E:\\PyProj\\Others\\rite_pos.txt")
frite = open("E:\\PyProj\\Others\\rite_event.txt")
fw = open("E:\\PyProj\\Others\\rite_3list.txt",'w')
pos = fpos.readline()
rite = frite.readline()
postagset = set()
eventtagset = set()
while(pos):
    #output
    word = []
    postag = []
    eventtag = []
    poss = pos.split(" ")
    for term in poss:
        terms = term.split('_')
        word.append(terms[0])
        postag.append(terms[1])
        eventtag.append('')
    for i in range(len(word)-1,-1,-1):
        startidx = rite.find(word[i])
        if(startidx == -1):
            eventtag[i] = 'O'
        while(startidx>=0):
            startidx-=1
            if(rite[startidx] == ']'or startidx== -1):
                eventtag[i] = 'O'
                break
            if(rite[startidx] == '['):
                j = startidx
                l = -1
                tag = ""
                while(j<len(rite)):
                    if(rite[j] == ' '):
                        l = j+1
                    if(rite[j] == ']'):
                        tag = rite[l:j]
                        break
                    j+=1
                eventtag[i] = tag
                break
    for k in word:
        fw.write(k+' ')
    fw.write('\n')
    for k in postag:
        k = k.replace('\n','')
        postagset.add(k)
        fw.write(k.replace('\n','')+' ')
    fw.write('\n')
    for k in eventtag:
        if(k==''):
            print pos
        eventtagset.add(k)
        fw.write(k+' ')
    fw.write('\n')
    pos = fpos.readline()
    rite = frite.readline()
fpos.close()
frite.close()
fw.close()
print eventtagset
print postagset