#-*-coding:utf-8-*-
__author__ = 'Administrator'
str = "[查尔斯 A]是非常[谨慎 EP]的人。"
# print str[1:10]
condition = 1
#1:read,2:left,3:tag,4:right,0:end
idx = 0#遍历str的索引号
tag = ""#记录当前tag
tagLeft = -1#当前tag起始字符的索引
tagRight = -1#当前tag末尾字符的后一个字符的索引
left = 0#[的索引
bTag = 0#是否处于tag中
right = 0#]的后一个字符的索引
word = ""#记录当前word
wordLeft = -1#当前词起始字符的索引
wordRight = -1#当前词末尾字符的后一个字符的索引

while(condition!=0):
    currChar = str[idx]
    if(currChar == '['):#进入left状态
        left = idx#记录[的索引
        idx += 1
        continue
    if(currChar == ' '):#进入Tag状态
        bTag = 1
        idx += 1
        continue
    if(bTag == 1):
        if(tagLeft == -1):
            tagLeft = idx#归0
        tag += str[idx]
        idx += 1
        continue
    #默认read状态
    if(wordLeft == -1):
        wordLeft = idx
    word += str[idx]
    idx += 1
