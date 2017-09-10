#!/usr/bin/env python3

import pandas as pd
import os
import numpy as np

#Gives average accuracy of each param set tested on inner loop data
def Pivot():
    dfs=pd.read_csv('/media/james/ext4data1/current/projects/pfizer/3151A1-303-csv2/deid_hamd17.csv')

    dfs2=dfs[dfs['CPENM']=='DAY 7']
    dfs3=dfs[dfs['CPENM']=='DAY 300']
    
    dfs2b= dfs2.pivot(index='PATIENT',columns='TESTS',values='VALN')
    dfs3b= dfs3.pivot(index='PATIENT',columns='TESTS',values='VALN')
    
    dfs2b['HAMD Total'].describe()

    return


'''
np.intersect1d(dfs2['PATIENT'],dfs['PATIENT'])
np.setdiff1d(dfs2['PATIENT'],dfs['PATIENT'])
'''

