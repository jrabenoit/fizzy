#!/usr/bin/env python3

import pandas as pd
import numpy as np
import os, pickle

#Gives average accuracy of each param set tested on inner loop data
def TestJoin():
    raw=pd.read_csv('/media/james/ext4data1/current/projects/pfizer/3151A1-303-csv2/deid_hamd17.csv')
    d7=raw[raw['CPENM']=='DAY 7']
    d300=raw[raw['CPENM']=='DAY 300']
    d7p= d7.pivot(index='PATIENT',columns='TESTS',values='VALN')
    d300p= d300.pivot(index='PATIENT',columns='TESTS',values='VALN')
    d7p.columns='Day 7: ' + df2b.columns
    d300p.columns='Day 300: ' + df3b.columns
   
    agg=pd.concat([df2b, df3b], axis=1, join='inner')
    #1136 subjects remain who have data in all columns
   
    data={}    
    for i in dfc.index:
        data[i]={}
    
    for i,j in zip(dfc.index, range(len(dfc.index))):
        data[i]['sx_d007']=dfc['Day 7: HAMD Total'][j]
        data[i]['sx_d300']=dfc['Day 300: HAMD Total'][j]
        
    for i in dfc.index:        
        if data[i]['sx_d007']>=14: mdd=True
        else: mdd=False
        
        if data[i]['sx_d300']<7 and mdd==True:
            data[i]['tx_remitter']=True
        else: data[i]['tx_remitter']=False
        
        if data[i]['sx_d300']<=(0.5*data[i]['sx_d007']) and mdd==True:
            data[i]['tx_responder']=True
        else: data[i]['tx_responder']=False
        
        if data[i]['sx_d300']>(0.5*data[i]['sx_d007']) and mdd==True:
            data[i]['tx_nonresponder']=True
        else: data[i]['tx_nonresponder']=False
        
    data=pd.DataFrame(data)
    data=data.transpose()
    
    data=pd.concat([data, dfc], axis=1, join='inner')
    
    with open('/media/james/ext4data1/current/projects/pfizer/vectors/data'+'.pickle', 'wb') as d:
        pickle.dump(data, d, pickle.HIGHEST_PROTOCOL) 
        
    return


    
'''
dfs2b['HAMD Total'].describe()
np.intersect1d(dfs2['PATIENT'],dfs['PATIENT'])
np.setdiff1d(dfs2['PATIENT'],dfs['PATIENT'])
'''

