import json
import os
import math
import numpy as np

j=''
path='../Visualization/data'

dd=[i for i in os.listdir(path)]
rt={}
rw={}
r={}
for j in dd:
    year=json.load(fp=open(path+'/'+j+'/year.json','r'))
    month=json.load(fp=open(path+'/'+j+'/month.json','r'))
    hour=json.load(fp=open(path+'/'+j+'/hour.json','r'))
    word=json.load(fp=open(path+'/'+j+'/word.json','r'))
    y={}
    m={}
    h={}
    w={}
    for i in year:
        y[i['year']]=i['count']
    for i in month:
        m[i['time']]=i['count']
    for i in hour:
        h[i['hour']]=i['count']
    for i in word:
        w[i['name']]=i['value']

    uid=[]
    y_score=[]
    m_score=[]
    h_score=[]
    w_score=[]
    for i in range(18):
        y_score.append([])
        m_score.append([])
        h_score.append([])
        w_score.append([])
    d=[i for i in os.listdir(path)]
    for ii in d:
        if (ii==j):
            continue
        uid.append(ii)
        y0=y.copy()
        m0=m.copy()
        h0=h.copy()
        w0=w.copy()
        
        ye=json.load(fp=open(path+'/'+ii+'/year.json','r'))
        mo=json.load(fp=open(path+'/'+ii+'/month.json','r'))
        ho=json.load(fp=open(path+'/'+ii+'/hour.json','r'))
        wo=json.load(fp=open(path+'/'+ii+'/word.json','r'))
        
        yy={}
        mm={}
        hh={}
        ww={}
        for i in ye:
            yy[i['year']]=i['count']
        for i in mo:
            mm[i['time']]=i['count']
        for i in ho:
            hh[i['hour']]=i['count']
        for i in wo:
            ww[i['name']]=i['value']
            
        for i in yy:
            if i not in y0:
                y0[i]=0
        for i in y0:
            if i not in yy:
                yy[i]=0
        for i in mm:
            if i not in m0:
                m0[i]=0
        for i in m0:
            if i not in mm:
                mm[i]=0
        for i in hh:
            if i not in h0:
                h0[i]=0
        for i in h0:
            if i not in hh:
                hh[i]=0
        for i in ww:
            if i not in w0:
                w0[i]=0
        for i in w0:
            if i not in ww:
                ww[i]=0

        y0= sorted(y0.items(), key=lambda i:i[0], reverse = False)
        m0= sorted(m0.items(), key=lambda i:i[0], reverse = False)
        h0= sorted(h0.items(), key=lambda i:i[0], reverse = False)
        w0= sorted(w0.items(), key=lambda i:i[0], reverse = False)
        yy= sorted(yy.items(), key=lambda i:i[0], reverse = False)
        mm= sorted(mm.items(), key=lambda i:i[0], reverse = False)
        hh= sorted(hh.items(), key=lambda i:i[0], reverse = False)
        ww= sorted(ww.items(), key=lambda i:i[0], reverse = False)
        
    #   print(y0)
    #   print(yy)
        y1=[]
        y2=[]
        m1=[]
        m2=[]
        h1=[]
        h2=[]
        w1=[]
        w2=[]
        for i in range(len(y0)):
            y1.append(y0[i][1])
            y2.append(yy[i][1])
        for i in range(len(m0)):
            m1.append(m0[i][1])
            m2.append(mm[i][1])
        for i in range(len(h0)):
            h1.append(h0[i][1])
            h2.append(hh[i][1])
        for i in range(len(w0)):
            w1.append(w0[i][1])
            w2.append(ww[i][1])

        y11=[]
        y22=[]
        m11=[]
        m22=[]
        h11=[]
        h22=[]
        w11=[]
        w22=[]

        for i in range(len(y1)):
            if (y1[i]>0):
                y11.append(1)
            else:
                y11.append(0)
            if (y2[i]>0):
                y22.append(1)
            else:
                y22.append(0)
        for i in range(len(m1)):
            if (m1[i]>0):
                m11.append(1)
            else:
                m11.append(0)
            if (m2[i]>0):
                m22.append(1)
            else:
                m22.append(0)
        for i in range(len(h1)):
            if (h1[i]>0):
                h11.append(1)
            else:
                h11.append(0)
            if (h2[i]>0):
                h22.append(1)
            else:
                h22.append(0)
        for i in range(len(w1)):
            if (w1[i]>0):
                w11.append(1)
            else:
                w11.append(0)
            if (w2[i]>0):
                w22.append(1)
            else:
                w22.append(0)
                
        #print(np.cov(a,b)[0,1]) #cov
        #print(np.corrcoef(a,b)[0][1]) #Pearson Correlation Coefficient
        #print(np.corrcoef(a,b)[0][1]/(scale)) #Pearson Correlation Coefficient / scale
        #print(np.linalg.norm(a-b)) #normal 
        #print(np.linalg.norm(a/max(a)-b/max(b))) #normal / max
        #print(np.linalg.norm(a/np.linalg.norm(a)-b/np.linalg.norm(b))) #normal / length
        #print(float(a.dot(b.T))/(np.linalg.norm(a) * np.linalg.norm(b))*0.5+0.5) #cos
        #print(float(aa.dot(bb.T))/(np.linalg.norm(aa) + np.linalg.norm(bb) - float(aa.dot(bb.T)))) # Jaccard
        #print(float(a.dot(b.T))/(np.linalg.norm(a) + np.linalg.norm(b) - float(a.dot(b.T)))) # Tanimoto
        #print(sum(abs(a-b))) # Manhattan
        #print(sum(abs(a/max(a)-b/max(b)))) # Manhattan / max
        #print(sum(abs(a/np.linalg.norm(a)-b/np.linalg.norm(b)))) # Manhattan / length
        #print(sum(abs(a-b)/(abs(a)+abs(b)))) # 兰式距离
        #print(sum(abs(a/max(a)-b/max(b))/(abs(a/max(a))+abs(b/max(b))))) # 兰式距离 / max
        #print(sum(abs(a/np.linalg.norm(a)-b/np.linalg.norm(b))/(abs(a/np.linalg.norm(a))+abs(b/np.linalg.norm(b))))) # 兰式距离 / length
        #print(max(abs(a-b))) # Chebyshev distance
        #print(max(abs(a/max(a)-b/max(b)))) # Chebyshev distance / max
        #print(max(abs(a/np.linalg.norm(a)-b/np.linalg.norm(b)))) # Chebyshev distance / length
        #print(max(max(min(abs(b-i)) for i in a),max(min(abs(a-i)) for i in b))) # Hausdorff  豪斯多夫距离
        # Standard Euclidean distance
        # Mahalanobis 马式距离
        # Minkowski  明可夫斯基距离
        
        s1=sum(y1)
        s2=sum(y2)
        scale=0
        if s1==0 or s2==0:
            scale=max(s1,s2)
        else:
            if s1>s2:
                scale=s1/s2
            else:
                scale=s2/s1
        a=np.array(y1)
        b=np.array(y2)
        aa=np.array(y11)
        bb=np.array(y22)
        #print(np.cov(a,b)[0,1]) #cov
        y_score[0].append(np.corrcoef(a,b)[0][1]) #Pearson Correlation Coefficient
        y_score[1].append(abs(np.corrcoef(a,b)[0][1])/(scale)) #Pearson Correlation Coefficient / scale
        y_score[2].append(np.linalg.norm(a-b)) #normal 
        y_score[3].append(np.linalg.norm(a/max(a)-b/max(b))) #normal / max
        y_score[4].append(np.linalg.norm(a/np.linalg.norm(a)-b/np.linalg.norm(b))) #normal / length
        y_score[5].append(float(a.dot(b.T))/(np.linalg.norm(a) * np.linalg.norm(b))*0.5+0.5) #cos
        y_score[6].append(float(aa.dot(bb.T))/(np.linalg.norm(aa) + np.linalg.norm(bb) - float(aa.dot(bb.T)))) # Jaccard
        y_score[7].append(float(a.dot(b.T))/(np.linalg.norm(a) + np.linalg.norm(b) - float(a.dot(b.T)))) # Tanimoto
        y_score[8].append(sum(abs(a-b))) # Manhattan
        y_score[9].append(sum(abs(a/max(a)-b/max(b)))) # Manhattan / max
        y_score[10].append(sum(abs(a/np.linalg.norm(a)-b/np.linalg.norm(b)))) # Manhattan / length
        y_score[11].append(sum(abs(a-b)/(abs(a)+abs(b)))) # 兰式距离
        y_score[12].append(sum(abs(a/max(a)-b/max(b))/(abs(a/max(a))+abs(b/max(b))))) # 兰式距离 / max
        y_score[13].append(sum(abs(a/np.linalg.norm(a)-b/np.linalg.norm(b))/(abs(a/np.linalg.norm(a))+abs(b/np.linalg.norm(b))))) # 兰式距离 / length
        y_score[14].append(max(abs(a-b))) # Chebyshev distance
        y_score[15].append(max(abs(a/max(a)-b/max(b)))) # Chebyshev distance / max
        y_score[16].append(max(abs(a/np.linalg.norm(a)-b/np.linalg.norm(b)))) # Chebyshev distance / length
        y_score[17].append(max(max(min(abs(b-i)) for i in a),max(min(abs(a-i)) for i in b))) # Hausdorff  豪斯多夫距离
        # Standard Euclidean distance
        # Mahalanobis 马式距离
        # Minkowski  明可夫斯基距离

        s1=sum(m1)
        s2=sum(m2)
        scale=0
        if s1==0 or s2==0:
            scale=max(s1,s2)
        else:
            if s1>s2:
                scale=s1/s2
            else:
                scale=s2/s1        
        a=np.array(m1)
        a=np.array(m1)
        b=np.array(m2)
        aa=np.array(m11)
        bb=np.array(m22)
        #print(np.cov(a,b)[0,1]) #cov
        m_score[0]. append(np.corrcoef(a,b)[0][1]) #Pearson Correlation Coefficient
        m_score[1].append(abs(np.corrcoef(a,b)[0][1])/(scale)) #Pearson Correlation Coefficient / scale
        m_score[2].append(np.linalg.norm(a-b)) #normal 
        m_score[3].append(np.linalg.norm(a/max(a)-b/max(b))) #normal / max
        m_score[4].append(np.linalg.norm(a/np.linalg.norm(a)-b/np.linalg.norm(b))) #normal / length
        m_score[5].append(float(a.dot(b.T))/(np.linalg.norm(a) * np.linalg.norm(b))*0.5+0.5) #cos
        m_score[6].append(float(aa.dot(bb.T))/(np.linalg.norm(aa) + np.linalg.norm(bb) - float(aa.dot(bb.T)))) # Jaccard
        m_score[7].append(float(a.dot(b.T))/(np.linalg.norm(a) + np.linalg.norm(b) - float(a.dot(b.T)))) # Tanimoto
        m_score[8].append(sum(abs(a-b))) # Manhattan
        m_score[9].append(sum(abs(a/max(a)-b/max(b)))) # Manhattan / max
        m_score[10].append(sum(abs(a/np.linalg.norm(a)-b/np.linalg.norm(b)))) # Manhattan / length
        m_score[11].append(sum(abs(a-b)/(abs(a)+abs(b)))) # 兰式距离
        m_score[12].append(sum(abs(a/max(a)-b/max(b))/(abs(a/max(a))+abs(b/max(b))))) # 兰式距离 / max
        m_score[13].append(sum(abs(a/np.linalg.norm(a)-b/np.linalg.norm(b))/(abs(a/np.linalg.norm(a))+abs(b/np.linalg.norm(b))))) # 兰式距离 / length
        m_score[14].append(max(abs(a-b))) # Chebyshev distance
        m_score[15].append(max(abs(a/max(a)-b/max(b)))) # Chebyshev distance / max
        m_score[16].append(max(abs(a/np.linalg.norm(a)-b/np.linalg.norm(b)))) # Chebyshev distance / length
        m_score[17].append(max(max(min(abs(b-i)) for i in a),max(min(abs(a-i)) for i in b))) # Hausdorff  豪斯多夫距离
        # Standard Euclidean distance
        # Mahalanobis 马式距离
        # Minkowski  明可夫斯基距离
        
        s1=sum(h1)
        s2=sum(h2)
        scale=0
        if s1==0 or s2==0:
            scale=max(s1,s2)
        else:
            if s1>s2:
                scale=s1/s2
            else:
                scale=s2/s1
        a=np.array(h1)
        b=np.array(h2)
        aa=np.array(h11)
        bb=np.array(h22)
        #print(np.cov(a,b)[0,1]) #cov
        h_score[0].append(np.corrcoef(a,b)[0][1]) #Pearson Correlation Coefficient
        h_score[1].append(abs(np.corrcoef(a,b)[0][1])/(scale)) #Pearson Correlation Coefficient / scale
        h_score[2].append(np.linalg.norm(a-b)) #normal 
        h_score[3].append(np.linalg.norm(a/max(a)-b/max(b))) #normal / max
        h_score[4].append(np.linalg.norm(a/np.linalg.norm(a)-b/np.linalg.norm(b))) #normal / length
        h_score[5].append(float(a.dot(b.T))/(np.linalg.norm(a) * np.linalg.norm(b))*0.5+0.5) #cos
        h_score[6].append(float(aa.dot(bb.T))/(np.linalg.norm(aa) + np.linalg.norm(bb) - float(aa.dot(bb.T)))) # Jaccard
        h_score[7].append(float(a.dot(b.T))/(np.linalg.norm(a) + np.linalg.norm(b) - float(a.dot(b.T)))) # Tanimoto
        h_score[8].append(sum(abs(a-b))) # Manhattan
        h_score[9].append(sum(abs(a/max(a)-b/max(b)))) # Manhattan / max
        h_score[10].append(sum(abs(a/np.linalg.norm(a)-b/np.linalg.norm(b)))) # Manhattan / length
        h_score[11].append(sum(abs(a-b)/(abs(a)+abs(b)))) # 兰式距离
        h_score[12].append(sum(abs(a/max(a)-b/max(b))/(abs(a/max(a))+abs(b/max(b))))) # 兰式距离 / max
        h_score[13].append(sum(abs(a/np.linalg.norm(a)-b/np.linalg.norm(b))/(abs(a/np.linalg.norm(a))+abs(b/np.linalg.norm(b))))) # 兰式距离 / length
        h_score[14].append(max(abs(a-b))) # Chebyshev distance
        h_score[15].append(max(abs(a/max(a)-b/max(b)))) # Chebyshev distance / max
        h_score[16].append(max(abs(a/np.linalg.norm(a)-b/np.linalg.norm(b)))) # Chebyshev distance / length
        h_score[17].append(max(max(min(abs(b-i)) for i in a),max(min(abs(a-i)) for i in b))) # Hausdorff  豪斯多夫距离
        # Standard Euclidean distance
        # Mahalanobis 马式距离
        # Minkowski  明可夫斯基距离
        
        s1=sum(w1)
        s2=sum(w2)
        scale=0
        if s1==0 or s2==0:
            scale=max(s1,s2)
        else:
            if s1>s2:
                scale=s1/s2
            else:
                scale=s2/s1
        a=np.array(w1)
        b=np.array(w2)
        aa=np.array(w11)
        bb=np.array(w22)
        #print(np.cov(a,b)[0,1]) #cov
        if s1==0 or s1==0:
            for i in range(18):
                w_score[i].append(0)
        else:
            w_score[0].append(np.corrcoef(a,b)[0][1]) #Pearson Correlation Coefficient
            w_score[1].append(abs(np.corrcoef(a,b)[0][1])/(scale)) #Pearson Correlation Coefficient / scale
            w_score[2].append(np.linalg.norm(a-b)) #normal 
            w_score[3].append(np.linalg.norm(a/max(a)-b/max(b))) #normal / max
            w_score[4].append(np.linalg.norm(a/np.linalg.norm(a)-b/np.linalg.norm(b))) #normal / length
            w_score[5].append(float(a.dot(b.T))/(np.linalg.norm(a) * np.linalg.norm(b))*0.5+0.5) #cos
            w_score[6].append(float(aa.dot(bb.T))/(np.linalg.norm(aa) + np.linalg.norm(bb) - float(aa.dot(bb.T)))) # Jaccard
            w_score[7].append(float(a.dot(b.T))/(np.linalg.norm(a) + np.linalg.norm(b) - float(a.dot(b.T)))) # Tanimoto
            w_score[8].append(sum(abs(a-b))) # Manhattan
            w_score[9].append(sum(abs(a/max(a)-b/max(b)))) # Manhattan / max
            w_score[10].append(sum(abs(a/np.linalg.norm(a)-b/np.linalg.norm(b)))) # Manhattan / length
            w_score[11].append(sum(abs(a-b)/(abs(a)+abs(b)))) # 兰式距离
            w_score[12].append(sum(abs(a/max(a)-b/max(b))/(abs(a/max(a))+abs(b/max(b))))) # 兰式距离 / max
            w_score[13].append(sum(abs(a/np.linalg.norm(a)-b/np.linalg.norm(b))/(abs(a/np.linalg.norm(a))+abs(b/np.linalg.norm(b))))) # 兰式距离 / length
            w_score[14].append(max(abs(a-b))) # Chebyshev distance
            w_score[15].append(max(abs(a/max(a)-b/max(b)))) # Chebyshev distance / max
            w_score[16].append(max(abs(a/np.linalg.norm(a)-b/np.linalg.norm(b)))) # Chebyshev distance / length
            w_score[17].append(max(max(min(abs(b-i)) for i in a),max(min(abs(a-i)) for i in b))) # Hausdorff  豪斯多夫距离
        # Standard Euclidean distance
        # Mahalanobis 马式距离
        # Minkowski  明可夫斯基距离
        
    #print(y_score[1])
    #print(m_score[1])
    #print(h_score[1])
    print('year')
    for i in range(len(h_score[1])):
        if y_score[1][i]==max(y_score[1]):
            print(uid[i])
    print('month')
    for i in range(len(m_score[1])):
        if m_score[1][i]==max(m_score[1]):
            print(uid[i])
    print('hour')
    for i in range(len(h_score[1])):
        if h_score[1][i]==max(h_score[1]):
            print(uid[i])
    print('word')
    for i in range(len(w_score[1])):
        if w_score[1][i]==max(w_score[1]):
            print(uid[i])
            rw[j]=uid[i]
    s=[]    
    for i in range(len(h_score[1])):
        s.append(y_score[1][i]*0.2+m_score[1][i]*0.5+h_score[1][i]*0.3)
    print('sum')
    for i in range(len(s)):
        if math.isnan(s[i]):
            s[i]=0
    for i in range(len(w_score[1])):
        if math.isnan(w_score[1][i]):
            w_score[1][i]=0
    #print(s)
    for i in range(len(s)):
        if s[i]==max(s):
            print(uid[i])
            rt[j]=uid[i]
    su=[]
    for i in range(len(s)):
        su.append(s[i]*0.5+w_score[1][i]*0.5)
    for i in range(len(su)):
        if su[i]==max(su):
            print(uid[i])
            r[j]=uid[i]
ft=open('../Visualization/reco/reco_time.json','w')
fw=open('../Visualization/reco/reco_word.json','w')
f=open('../Visualization/reco/reco.json','w')
ft.write(json.dumps(rt))
fw.write(json.dumps(rw))
f.write(json.dumps(r))
ft.close()
fw.close()
f.close()