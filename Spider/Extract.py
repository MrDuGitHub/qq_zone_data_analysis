import json
import os
import xlwt
import pymysql
import time
from datetime import datetime
import json
import codecs
import re

def Extract():
    d=[i for i in os.listdir('../Spider/mood_detail') if not i.endswith('.xls')]
    for ii in d:
        if not os.path.exists('../Spark/data/'+ii):
            os.mkdir('../Spark/data/'+ii)
        f=codecs.open('../Spark/data/'+ii+'/'+'time.txt','w','utf-8')
        fcs=codecs.open('../Spark/data/'+ii+'/'+'content.txt','w','utf-8')
        fl=[i for i in os.listdir('../Spider/mood_detail/'+ii) if i.endswith('.json')]
        for i in fl:
            #print('../Spider/mood_detail/'+ii+'/'+i[0:-5]+'_time.txt')
            with open('../Spider/mood_detail/'+ii+"/"+i,'r',encoding='utf-8') as w:
                s=w.read()[17:-2]
                js=json.loads(s)
                for s in js['msglist']:
                    print(s['createTime'])
                    f.write(str(s['created_time'])+'\n')
                    emoji = re.compile(r'e\d+'))
                    ss = emoji.sub('',s['content'])
                    ss=ss.replace("[em/]","").replace("[/em]","").replace("[em]","").replace("\n","/n")
                    fcs.write(ss+'\n')
    f.close()
    fcs.close()
Extract()
