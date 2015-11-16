__author__ = 'Administrator'
eventTag = ['A', 'Ma', 'D', 'P', 'Ai', 'M', 'L', 'O', 'Re', 'Ra', 'Th', 'I', 'Rn', 'Cau', 'EP', 'T']
#string = "O A O EP O Re Re Re Re Re Re Re Re Re Re O Re Re Re Re Re Re Re Re Re Re Re O A Re Re Re Re Re Re Re O "
string = "O A O EP "
strs = string.rstrip().split(" ")
data = []
for i in strs:
    data.append(eventTag.index(i))
print data