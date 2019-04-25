# -*- coding: utf-8 -*-
from soynlp.lemmatizer import Lemmatizer
from konlpy.tag import Twitter

twitter = Twitter()
stems = {}
with open('lemma_dict.txt', 'r', encoding='UTF8') as lemmafile:
	stems = { line.replace('\n', '') for line in lemmafile.readlines()}

lmm = Lemmatizer(stems=stems, endings=[])

# change to os.walk
for i in ["namu_movie", "namu_tv", "namu_drama", "naver"]:
	
	with open('{}.txt'.format(i), 'r', encoding="UTF8") as openfile:
		with open('datalemm/{}.txt'.format(i), 'w', encoding="UTF8") as outfile:
			lines = openfile.readlines()
			print('line read finished')
			
			for line in lines:
				texts = []
				data = twitter.pos(line)
				unlemmatizable = set()
				for d in data:
					if d[1] == 'Adjective':
						lemmatized = lmm.lemmatize(d[0],check_only_stem=True)
						if len(lemmatized) > 0:
							texts.append(next(iter(lemmatized))[0])
						else:
							texts.append(d[0])
					else:
						texts.append(d[0])
				outfile.write(" ".join(texts))
		print("lemma finished for :{}".format(i))
