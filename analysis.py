#coding:utf-8
import math
import sys  
import jieba
reload(sys)  
sys.setdefaultencoding('utf8')   
f = open('wordic.txt')
p = open('wordicout.txt')
fpos = open('pnn_annotated.txt')
dic = []
dicout = []
coutpos = 0
coutneg = 0
coutneu = 0

'''
pos = open('possentence.txt','wb')
neg = open('negsentence.txt','wb')
neu = open('neusentence.txt','wb')

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
pos.close
neg.close
neu.close
'''

pos = open('possentence.txt')
neg = open('negsentence.txt')
neu = open('neusentence.txt')

for line in f:   
    dic.append(line.strip('\n'))

for line in p:
    dicout.append(int(line.strip('\n')))

num = 100

ration = 0
cout = 0
for line in pos:
    cout += 1
    total = 0
    words = jieba.cut(line)
    for word in words:
        if word in dic:
            total += dicout[dic.index(word)]    # 计算句子的情感得分

    if total > 5:
        ration += 1
    if cout > num:
            break
print('pos correct ration: ', ration/ (num * 1.0))

ration = 0
cout = 0
for line in neg:
    cout += 1
    total = 0
    words = jieba.cut(line)
    for word in words:
        if word in dic:
            total += dicout[dic.index(word)]

    if total < -5:
        ration += 1
    if cout > num:
        break


print('neg correct ration: ', ration/ (num * 1.0))

cout = 0
ration = 0
for line in neu:
    cout += 1
    total = 0
    words = jieba.cut(line)
    for word in words:
        if word in dic:
            total += dicout[dic.index(word)]

    if total >= -5 and total <= 5:
        ration += 1
    if cout > num:
            break


print('neu correct ration: ', ration/ (num * 1.0))
