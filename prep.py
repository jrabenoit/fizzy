#!/usr/bin/env python3

import pandas as pd

#Gives average accuracy of each param set tested on inner loop data
def Framer():
    
    df1=pd.read_csv('/media/james/ext4data1/current/projects/pfizer/3151A1-303-csv/deid_adverse.csv')
    df2=pd.read_csv('/media/james/ext4data1/current/projects/pfizer/3151A1-303-csv/deid_hamd17.csv')

    cdf=pd.merge(df1, df2, how='outer', left_on=['PATIENT'], right_on=['CPENM'])
    
    cdf.to_csv('/media/james/ext4data1/current/projects/pfizer/cdf.csv')
    
    return
