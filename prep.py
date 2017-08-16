#!/usr/bin/env python3

import pandas as pd
import os
import numpy as np

#Gives average accuracy of each param set tested on inner loop data
def Cutter():
    for i in os.listdir('/media/james/ext4data1/current/projects/pfizer/3151A1-303-csv2/'):    
        df1=pd.read_csv('/media/james/ext4data1/current/projects/pfizer/3151A1-303-csv2/'+str(i), encoding='utf-8')
        if 'RELDAYU' in df1.keys(): df1= df1.drop('RELDAYU', 1)
        
        df1.to_csv('/media/james/ext4data1/current/projects/pfizer/3151A1-303-csv2/'+str(i))    
    return

def Framer():    
    dfs=pd.read_csv('/media/james/ext4data1/current/projects/pfizer/deid_adverse.csv', encoding='utf-8')
    c=0
    for i in os.listdir('/media/james/ext4data1/current/projects/pfizer/3151A1-303-csv/'):
        c=c+1
        print('{}/45'.format(c))
        df1=pd.read_csv('/media/james/ext4data1/current/projects/pfizer/3151A1-303-csv/'+str(i), encoding='utf-8')
        if ('PATIENT' in df1.keys() and 'CPENM' in df1.keys()):
            dfs=pd.merge(dfs, df1, how='left', on=['PATIENT', 'CPENM'])
            dfs=dfs.drop_duplicates()
    pd.to_csv(dfs, '/media/james/ext4data1/current/projects/pfizer/cdf.csv')
    return
