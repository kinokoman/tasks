import time
import csv

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

answers=[]
for x in range(len(texts)):
	answer=0
	for y in range(len(words)):
		for z in range(len(texts[0])):
			if words[y][0]==texts[x][z:z+len(words[y][0])]:
				answer+=int(words[y][1])
	answers.append(answer)
	
finish = time.time()
time = finish - start

f = open('answer2.txt', 'w')
for say in answers:
	f.write(str(say)+ "\n")

f.write(str(time))
f.close()
