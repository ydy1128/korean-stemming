# -*- coding: utf-8 -*-

from konlpy.tag import Twitter
import os

twitter = Twitter()

data = []

#change to os.walk
dirnames = ["namu_movie", "namu_tv", "namu_drama", "naver"]

for dirname in dirnames:
	print("parse start for: {}".format(dirname))
	path = '/home/dyyoon/Documents/parse/{}/'.format(dirname)
	for filename in os.listdir(path):
		with open('/home/dyyoon/Documents/parse/{}/{}'.format(dirname, filename), 'r') as openfile:
			lines = []
			try:
				lines = openfile.readlines()
			except UnicodeDecodeError:
				continue
			for line in lines:
				tagged = twitter.pos(line)
				data.append(tagged)
	with open('./{}.txt'.format(dirname), 'w', encoding="utf-8") as outfile:
		prev = ("", "")
		for d_list in data:
			for d in d_list:
				#Punctuation중 이어나오지않는 .과 ,만 남긴다
				if prev[1] == "Punctuation" and d[1] == "Punctuation":
					continue
				if d[1] == "Punctuation" and d[0] in [",", "."]:
					if d[0] == ".":
						outfile.write("{}\n".format(d[0]))
					else:
						outfile.write(d[0])
				#어미 조사 외국어(중국어, 일본어 등) 표식등 제외
				if d[1] not in ["Josa", "Suffix", "Eomi", "KoreanParticle", "Foreign", "Punctuation"]:
					outfile.write(" {}".format(d[0]))
				prev = d
	data = []
	print('file write: {} finished'.format(dirname))