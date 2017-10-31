#!/usr/bin/env python3

import pandas as pd
import os
import numpy as np

def Framer():    
    data=pd.read_csv('/media/james/ext4data1/current/projects/pfizer/3151A1-303-csv/deid_adverse.csv', encoding='utf-8')
    
    for i in os.listdir('/media/james/ext4data1/current/projects/pfizer/3151A1-303-csv'):
        info=pd.read_csv('/media/james/ext4data1/current/projects/pfizer/3151A1-303-csv/'+str(i), encoding='utf-8')
        data=pd.merge(data, info, how='left', on=['PATIENT', 'CPENM'])
        data=data.drop_duplicates()
    
    pd.to_csv(data, '/media/james/ext4data1/current/projects/pfizer/data.csv')
    
    return
