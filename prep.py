#!/usr/bin/env python3

import pandas as pd
import os, scipy.stats
import numpy as np

def Agglomerate():
    discrete= ['deid_adverse', 'deid_aemeddra', 'deid_cgi', 'deid_demow', 'deid_diaghist', 'deid_hamd17', 'deid_hamd17a', 'deid_labbase', 'deid_maddrs', 'deid_medhist', 'deid_medhist2', 'deid_nsmed', 'deid_othtrt', 'deid_physexam', 'deid_sdi', 'deid_stdymedw', 'deid_whowbi']

   # continuous= [deid_demow, deid_ecgbase, deid_ecgtest, ded_labbase, deid_labtest, deid_qtcn, deid_qtcnbase, deid_stdymedw, deid_vas2, deid_vittest]
    
    for i in discrete:
        info=pd.read_csv('/media/james/ext4data1/current/projects/pfizer/3151A1-303-csv/'+str(i)+'.csv', encoding='utf-8')
        a= info[info['CPENM']=='DAY 7']
        b= a.set_index(['PATIENT'])
        c= pd.get_dummies(b)
        
        d= {}
        for i in list(set(c.index)):
            d[i]= c.loc[i].values.flatten()
        
        maxlen=len(d[max(d, key=lambda k: len(d[k]))])    
        
        for i in d:
            d[i]=np.append(d[i], [0]*(maxlen-len(d[i])))        
        d= pd.DataFrame.from_dict(d, orient='index')
        d.columns=list(c.columns)*scipy.stats.mode(c.index).count[0]
        
        #this gives a dataframe with all variables binarized
        
    return
    
    df.values.flatten


    
        
        
