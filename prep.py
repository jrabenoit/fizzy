#!/usr/bin/env python3

import pandas as pd
import os
import numpy as np
import dask.dataframe as dd

#Gives average accuracy of each param set tested on inner loop data
def Framer():
    
    dfs=dd.read_csv('/media/james/ext4data1/current/projects/pfizer/deid_adverse.csv', encoding='utf-8')
    c=1
    
    for i in os.listdir('/media/james/ext4data1/current/projects/pfizer/3151A1-303-csv/'):
        print('{}/45, {}'.format(c,i))
        c=c+1
        check= pd.DataFrame.from_csv('/media/james/ext4data1/current/projects/pfizer/3151A1-303-csv/'+str(i), encoding='utf-8')
        df1=dd.read_csv('/media/james/ext4data1/current/projects/pfizer/3151A1-303-csv/'+str(i), encoding='utf-8')
        if ('PATIENT' in check.keys() and 'CPENM' in check.keys()):
            dfs=dd.merge(dfs, df1, how='outer', on=['PATIENT'])
    
    dfs= dfs.apply(pd.to_numeric, errors='coerce', axis=1)

    #dd.to_csv(dfs, '/media/james/ext4data1/current/projects/pfizer/cdf.csv')

    return
