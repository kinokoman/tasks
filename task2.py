import time
import csv
import re
from multiprocessing import Pool

start = time.time()

f = open('large_text.txt')
texts = f.readlines()
f.close()

for x in range(len(texts)):
	texts[x]=texts[x].replace('\n','')
	texts[x]=texts[x].replace('\r','')

words=[]
with open("./words.tsv") as rf:
    reader = csv.reader(rf, delimiter="\t")
    for row in reader:
        words.append(row)

def function(x):
	answer=0
	for y in range(len(words)):
		answer+=int(words[y][1]) * len(re.findall('(?='+words[y][0]+')', texts[x]))
	return answer

def multi(n):
    p = Pool(10)
    result = p.map(function, range(n))
    return result

def main(hoge):
    answers = multi(100)
    finish = time.time()
    zikan = finish - hoge
    f = open('answer2_2.txt', 'w')
    for say in answers:
		f.write(str(say)+ "\n")
    f.write(str(zikan))
    f.close()

main(start)
