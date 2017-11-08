#!/usr/bin/env python3

import pandas as pd
import numpy as np
import os, pickle

#Remember we'll need to pivot so all the vals are on a single row.
    

def Groups():
    hamd=pd.read_csv('/media/james/ext4data1/current/projects/pfizer/3151A1-303-csv/deid_hamd17.csv')
    d60=hamd[hamd['CPENM']=='DAY 60']
    d60p= d60.pivot(index='PATIENT',columns='TESTS',values='VALN')
       
    mddict={}
    for i in d60p.index:        
        if d60p.loc[i,'HAMD Total']<=7: mdd=0
        else: mdd=1
        mddict[i]=mdd
        
    groups=pd.DataFrame.from_dict(mddict, orient='index')
    groups.index.name='PATIENT'
    groups.columns= ['GROUPLABEL']
        
    groups.to_csv(path_or_buf='/media/james/ext4data1/current/projects/pfizer/groups.csv', index_label='PATIENT')
        
    return


    
'''
#Descriptive statistics: central tendency, dispersion and shape
dfs2b['HAMD Total'].describe()

#Returns vals in df1 that are also in df2
np.intersect1d(df1['PATIENT'],df2['PATIENT'])

#Returns vals in df1 that are not in df2
np.setdiff1d(df1['PATIENT'],df2['PATIENT'])
'''

