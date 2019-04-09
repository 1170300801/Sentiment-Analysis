#coding:utf-8
import math
import jieba
import sys  
reload(sys)  
sys.setdefaultencoding('utf-8')   
fpos = open('pnn_annotated.txt')
dicstop = open('stopwords.txt','r')
dictotal = []
dic1 = []
dic2 = []
dic = []
stop = []

for line in dicstop:
    line = line.strip('\r\n')
    stop.append(line)

cout = 0
for line in fpos:
    line = line.strip('\n')
    num = int(line[0:2])
    line = line[2:]
    words = jieba.cut(line)
    for word in words:
        if word not in stop and num > 0:
            dic1.append(word)
            dictotal.append(word)
        elif word not in stop and num < 0:
            dic2.append(word)
            dictotal.append(word)
        if word in stop:
            print("yes")

f = open('wordic.txt','wb')
p = open('wordicout.txt','wb')
dic = list(set(dictotal))

for i in range(len(dic)):
    total = dic1.count(dic[i]) + dic2.count(dic[i])
    differ = dic1.count(dic[i]) - dic2.count(dic[i])
    weight = int(pow(3, float(pow(abs(differ), 1.0/3) * abs(differ)) / total))
    
    if total == 1:
        f.write(dic[i] + '\n')
        p.write(str(differ) + '\n')

    elif differ > 1:
        f.write( dic[i] + '\n')
        if weight > 1:
            p.write(' ' + str(weight) + '\n')
        else:
            p.write('0' + '\n')

    
    elif differ < -1:
        f.write(dic[i] + '\n')
        if weight > 1:
            p.write(' -' + str(weight) + '\n')
        else:
            p.write('0' + '\n')



f.close
p.close
