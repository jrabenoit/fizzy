#!/usr/bin/env python3

import pandas as pd
import os
import numpy as np

def Agglomerate():
    for i in os.listdir('/media/james/ext4data1/current/projects/pfizer/3151A1-303-csvtest'):
        info=pd.read_csv('/media/james/ext4data1/current/projects/pfizer/3151A1-303-csvtest/'+str(i), encoding='utf-8')
        a= info[info['CPENM']=='DAY 7']
        b= info.set_index(['PATIENT'])
        c= pd.get_dummies(b)
        d= c.groupby(c.index).sum()
        
    return

