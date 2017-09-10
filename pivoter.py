#!/usr/bin/env python3

import pandas as pd
import numpy as np
import os, pickle

#Gives average accuracy of each param set tested on inner loop data
def Pivot():
    df=pd.read_csv('/media/james/ext4data1/current/projects/pfizer/3151A1-303-csv2/deid_hamd17.csv')

    df2=df[df['CPENM']=='DAY 7']
    df3=df[df['CPENM']=='DAY 300']
    
    df2b= df2.pivot(index='PATIENT',columns='TESTS',values='VALN')
    df3b= df3.pivot(index='PATIENT',columns='TESTS',values='VALN')

    df2b.columns='Day 7: ' + df2b.columns
    df3b.columns='Day 300: ' + df3b.columns
    
    dfc=pd.concat([df2b, df3b], axis=1, join='inner')
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
        
    
    #We want to restructure the shopvec code so we can just create columns in the existing "dfc" dataframe rather than making a secondary dict, "data". This is just to fit it into the existing shopvec code for now.
    #data=pd.DataFrame(data)
    
    with open('/media/james/ext4data1/current/projects/pfizer/vectors/data'+'.pickle', 'wb') as d:
        pickle.dump(data, d, pickle.HIGHEST_PROTOCOL) 
    with open('/media/james/ext4data1/current/projects/pfizer/vectors/dfc'+'.pickle', 'wb') as d:
        pickle.dump(dfc, d, pickle.HIGHEST_PROTOCOL) 
    return

'''
with open('/media/james/ext4data1/current/projects/pfizer/vectors/dfc.pickle', 'rb') as f:
    dfc= pickle.load(f)
with open('/media/james/ext4data1/current/projects/pfizer/vectors/data.pickle', 'rb') as f:
    data= pickle.load(f)

dfs2b['HAMD Total'].describe()
np.intersect1d(dfs2['PATIENT'],dfs['PATIENT'])
np.setdiff1d(dfs2['PATIENT'],dfs['PATIENT'])
'''

