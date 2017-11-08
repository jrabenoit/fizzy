#!/usr/bin/env python3

import pandas as pd
import os, scipy.stats
import numpy as np

def Binarize():
    csv= ['deid_adverse', 'deid_aemeddra', 'deid_medhist', 'deid_medhist2', 'deid_nsmed', 'deid_othtrt']

    for i in csv:
        info=pd.read_csv('/media/james/ext4data1/current/projects/pfizer/3151A1-303-csv/'+str(i)+'.csv', encoding='utf-8')
        a= info.set_index(['PATIENT'])
        b= pd.get_dummies(a)
        
        d= {}
        for j in list(set(b.index)):
            d[j]= b.loc[j].values.flatten()
        
        maxlen=len(d[max(d, key=lambda k: len(d[k]))])    
        
        for m in d:
            d[m]=np.append(d[m], [0]*(maxlen-len(d[m])))        
        
        d= pd.DataFrame.from_dict(d, orient='index')
        d.columns=list(b.columns)*scipy.stats.mode(b.index).count[0]
        #this gives a dataframe with all variables binarized
        
        d.to_csv(path_or_buf='/media/james/ext4data1/current/projects/pfizer/vecs/vecs_'+str(i)+'.csv', index_label='PATIENT')

    return

def Groups():
    hamd=pd.read_csv('/media/james/ext4data1/current/projects/pfizer/3151A1-303-csv all patients all days/deid_hamd17.csv')
    d60=hamd[hamd['CPENM']=='DAY 60']
    d60p= d60.pivot(index='PATIENT',columns='TESTS',values='VALN')
       
    mddict={}
    for i in d60p.index:        
        if d60p.loc[i,'HAMD Total']<=7: mdd=0
        else: mdd=1
        mddict[i]=mdd
        
    groups=pd.DataFrame.from_dict(mddict, orient='index')
    groups.columns= ['GROUPLABEL']
    info.set_index(['PATIENT'])
        
    groups.to_csv(path_or_buf='/media/james/ext4data1/current/projects/pfizer/groups.csv', index_label='PATIENT')
        
    return


def Homeopathy():
    #Cuts all tables to Placebo subjects
    info=pd.read_csv('/media/james/ext4data1/current/projects/pfizer/placebos.csv', encoding='utf-8')
    placebos= list(info['PATIENT'])
    
    path= '/media/james/ext4data1/current/projects/pfizer/vecs/'
    csvs= os.listdir(path)
    for i in csvs:
        a= pd.read_csv(path+i)
        b= a[a['PATIENT'].isin(placebos)]
        b= b.set_index('PATIENT')
        b.to_csv(path_or_buf='/media/james/ext4data1/current/projects/pfizer/vecs_placebos/placebos_'+str(i), index_label='PATIENT')
    
    return


def Harvester():
    '''Because it's a combine. Aha. Ha.'''
    info=pd.read_csv('/media/james/ext4data1/current/projects/pfizer/placebos.csv', encoding='utf-8')
    info=info.set_index('PATIENT')

    path= '/media/james/ext4data1/current/projects/pfizer/vecs_placebos/'
    csvs= os.listdir(path)
    
    for i in csvs:
        a=pd.read_csv(path+i)
        a=a.set_index('PATIENT')
        info=pd.concat([info, a], axis=1)
    
    info
    
    info.to_csv(path_or_buf='/media/james/ext4data1/current/projects/pfizer/final_vecs.csv', index_label='PATIENT')
    
    return


    
'''
#Descriptive statistics: central tendency, dispersion and shape
dfs2b['HAMD Total'].describe()

#Returns vals in df1 that are also in df2
np.intersect1d(df1['PATIENT'],df2['PATIENT'])

#Returns vals in df1 that are not in df2
np.setdiff1d(df1['PATIENT'],df2['PATIENT'])
'''
