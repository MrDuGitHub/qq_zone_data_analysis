import os
import sys
import time
import json

from pyspark import SparkConf, SparkContext
from pyspark.sql import SparkSession

spark= SparkSession.builder.master('local').appName('test').getOrCreate()
sc = spark.sparkContext
sc.setLogLevel('OFF')

d=[i for i in os.listdir('data')]
for ii in d:
	rdd=spark.read.text(paths = 'file:///E:/Git/qq_zone_date_analysis/Spark/data/'+ii+'/time.txt').rdd
	if not os.path.exists('../Visualization/data/'+ii):
		os.mkdir('../Visualization/data/'+ii)
	yearColl = rdd.map(lambda word:(time.strftime("%Y_%m_%d %H:%M:%S", time.localtime(int(word.value)))[0:4],1)).reduceByKey(lambda a,b:a+b).collect()
	# rdd转为collecton并打印
	result=[]
	min=2020
	max=1980
	for line in yearColl:
		year={}
		year['year']=int(line[0][0:4])
		if (int(line[0][0:4])>max):
			max=int(line[0][0:4])
		if (int(line[0][0:4])<min):
			min=int(line[0][0:4])
		year['count']=int(line[1])
		result.append(year)
	for i in range(min,max+1):
		exist=False
		for j in result:
			if j['year']==i:
				exist=True
				break
		if (not exist):
			year={}
			year['year']=i
			year['count']=0
			#result.append(year)
	result.sort(key = lambda x:x["year"])
	print(json.dumps(result))
	fp=open('../Visualization/data/'+ii+'/year.json','w')
	fp.write(json.dumps(result))
	fp.close()
	
	monthColl = rdd.map(lambda word:(time.strftime("%Y_%m_%d %H:%M:%S", time.localtime(int(word.value)))[0:7],1)).reduceByKey(lambda a,b:a+b).collect()
	# rdd转为collecton并打印
	result=[]
	y=[]
	for line in monthColl:
		month={}
		month['year']=int(line[0][0:4])
		month['month']=int(line[0][5:7])
		month['time']=line[0][0:7]
		month['count']=int(line[1])
		y.append(int(line[0][0:4]))
		result.append(month)
	for i in y:
		for j in range(1,13):
			exist=False
			if (j<10):
				t=str(i)+'_0'+str(j)
			else:
				t=str(i)+'_'+str(j)
			for k in result:
				if k['time']==t:
					exist=True
					break
			if (not exist):
				month={}
				month['year']=i
				month['month']=j
				month['time']=t
				month['count']=0
				result.append(month)
	result.sort(key = lambda x:x["time"])
	for i in range(len(result)):
		result[i]['id']=i;
	print(json.dumps(result))
	fp=open('../Visualization/data/'+ii+'/month.json','w')
	fp.write(json.dumps(result))
	fp.close()
	
	dayColl = rdd.map(lambda word:(time.strftime("%Y_%m_%d %H:%M:%S", time.localtime(int(word.value)))[8:10],1)).reduceByKey(lambda a,b:a+b).collect()
	# rdd转为collecton并打印
	result=[]
	for line in dayColl:
		day={}
		day['day']=int(line[0])
		day['count']=int(line[1])
		result.append(day)
	for i in range(1,32):
		exist=False
		for j in result:
			if j['day']==i:
				exist=True
				break
		if (not exist):
			day={}
			day['day']=i
			day['count']=0
			result.append(day)
	result.sort(key = lambda x:x["day"])
	print(json.dumps(result))
	fp=open('../Visualization/data/'+ii+'/day.json','w')
	fp.write(json.dumps(result))
	fp.close()
	
	hourColl = rdd.map(lambda word:(time.strftime("%Y_%m_%d %H:%M:%S", time.localtime(int(word.value)))[11:13],1)).reduceByKey(lambda a,b:a+b).collect()
	# rdd转为collecton并打印
	result=[]
	for line in hourColl:
		hour={}
		hour['hour']=int(line[0])
		hour['count']=int(line[1])
		result.append(hour)
	for i in range(0,24):
		exist=False
		for j in result:
			if j['hour']==i:
				exist=True
				break
		if (not exist):
			hour={}
			hour['hour']=i
			hour['count']=0
			result.append(hour)
	result.sort(key = lambda x:x["hour"])
	print(json.dumps(result))
	fp=open('../Visualization/data/'+ii+'/hour.json','w')
	fp.write(json.dumps(result))
	fp.close()
	
sc.stop()
	# 结束
