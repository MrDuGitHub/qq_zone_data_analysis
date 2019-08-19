from pyhanlp import * 
import codecs;
import json
# 共性分析

d=[i for i in os.listdir('data')]
num=1
for ii in d:
	print(num)
	num+=1
	fp=codecs.open('data/'+ii+'/content.txt','r','utf-8')
	y=fp.readlines()

	Occurrence = JClass("com.hankcs.hanlp.corpus.occurrence.Occurrence")
	#PairFrequency = JClass("com.hankcs.hanlp.corpus.occurrence.PairFrequency")
	#TermFrequency = JClass("com.hankcs.hanlp.corpus.occurrence.TermFrequency")
	#TriaFrequency = JClass("com.hankcs.hanlp.corpus.occurrence.TriaFrequency")

	occurrence = Occurrence()
	for i in y:
		occurrence.addAll(i.replace("em","").replace("e",""))
	occurrence.compute()

	#print("一阶共性分析，也就是词频统计")
	fp=open('../Visualization/data/'+ii+'/word.json','w')
	l=[]
	name=[]
	data=[]
	j=[]
	stopword=['n','%','a','R','%E','<R','uin','nick','@','http','com','www','url','cn','#http','#','-','_','__','`']
	unigram = occurrence.getUniGram()
	for entry in unigram.iterator():
		term_frequency = entry.getValue()
		name.append(str(term_frequency)[0:str(term_frequency).index('=')])
		l.append(int(str(term_frequency)[(str(term_frequency).index('=')+1):len(str(term_frequency))]))
	##print(name)
	##print(l)
	for i in range(len(name)):
		if name[i] not in stopword and l[i]>3:
			d={}
			d['name']=name[i]
			d['value']=l[i]*10
			#d['item_style']='createRandomItemStyle()'
			j.append(d)
			data.append((name[i],l[i]))
	l=sorted(data,key = lambda x:x[1],reverse = True)
	#print(l)
	fp.write(json.dumps(j))
	fp.close()