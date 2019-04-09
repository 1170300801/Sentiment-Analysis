#coding:utf-8
import math
import sys  
import jieba
reload(sys)  
sys.setdefaultencoding('utf8')   
f = open('wordic.txt')
#pos = open('possentence.txt','wb')
#neg = open('negsentence.txt','wb')
#neu = open('neusentence.txt','wb')
p = open('wordicout.txt')
w = open('result.txt','wb')
fpos = open('pnn_annotated.txt')
dic = []
dicout = []
coutpos = 0
coutneg = 0
coutneu = 0

'''
for line in fpos:
    line = line.strip('\n')
    num = int(line[0:2])
    line = line[2:]
    if num == 0:
        neu.write(line + '\n')
        coutneu += 1
    elif num == 1:
        pos.write(line + '\n')
        coutpos += 1
    else:
        neg.write(line[1:] + '\n')
        coutneg += 1
'''
#pos.close
#neg.close
#neu.close

pos = open('possentence.txt')
neg = open('negsentence.txt')
neu = open('neusentence.txt')

for line in f:   
    dic.append(line.strip('\n'))

for line in p:
    dicout.append(int(line.strip('\n')))

ration = 0
'''
for line in pos:
    total = 0
    words = jieba.cut(line)
    for word in words:
        if word in dic:
            total += dicout[dic.index(word)]

    if total >= 3:
        ration += 1

print('pos correct ration: ', ration/50.0)

ration = 0
for line in neg:
    total = 0
    words = jieba.cut(line)
    for word in words:
        if word in dic:
            total += dicout[dic.index(word)]

    if total <= -3:
        ration += 1

print('neg correct ration: ', ration/50.0)
'''
ration = 0
for line in neu:
    total = 0
    words = jieba.cut(line)
    for word in words:
        if word in dic:
            total += dicout[dic.index(word)]
            print(word)
            print(dicout[dic.index(word)])
    print(total)
    print("")

    if total > -3 and total < 3:
        ration += 1

print('neu correct ration: ', ration/50.0)
