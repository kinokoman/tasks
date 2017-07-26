#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time
import re
from multiprocessing import Pool

#開始時間を記録
start = time.time()

#textファイルを開いてデータを読み込む
f = open('large_text.txt')
texts = f.readlines()
f.close()

#各テキストから余計な改行を省く
for x in range(len(texts)):
	texts[x]=texts[x].replace('\n','')
	texts[x]=texts[x].replace('\r','')

#wordsファイルを開いてデータを読み込む
f = open('words.tsv')
words = f.readlines()
f.close()

#各ワードから余計な改行を省いてワードと点数を分離
for x in range(len(words)):
	words[x]=words[x].replace('\n','')
	words[x]=words[x].replace('\r','')
	words[x]=words[x].split("\t")

#テキストに各ワードが含まれているか検索して含まれている数だけ点数追加
def serch(x):
	answer=0
	for y in range(len(words)):
		answer+=int(words[y][1]) * len(re.findall('(?='+words[y][0]+')', texts[x]))
	return answer

#並列処理を行う時の最大プロセス数を指定
p = Pool(10)

#serch関数を並列処理で全テキスト同時に実行
answers = p.map(serch, range(len(texts)))

#終了時間を記録
finish = time.time()

#実行時間を算出
time = finish - start

#各テキストの点数と実行時間をanswerファイルに書き込む
f = open('answer2_2.txt', 'w')
for answer in answers:
	f.write(str(answer)+ "\n")
f.write(str(time))
f.close()
