# -*-coding:utf-8-*-
__author__ = 'ZhangHe'

pos = "迪士尼_nh 创始人_n 之一_r 华特_nh 迪士尼_nh 获_v 颁奥斯卡_n 特别_d 成就奖_v 。_wp"
rite = "迪士尼创始人之一[华特迪士尼 A][获颁 EP][奥斯卡特别成就奖 P]。"
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
for i in range(len(word) - 1, -1, -1):
    startidx = rite.find(word[i])
    if(startidx == -1):
        eventtag[i] = 'O'
    while (startidx >= 0):
        startidx -= 1
        if (rite[startidx] == ']' or startidx== -1):
            eventtag[i] = 'O'
            break
        if (rite[startidx] == '['):
            j = startidx
            l = -1
            tag = ""
            while (j < len(rite)):
                if (rite[j] == ' '):
                    l = j + 1
                if (rite[j] == ']'):
                    tag = rite[l:j]
                    break
                j += 1
            eventtag[i] = tag
            break
print word
print postag
print eventtag