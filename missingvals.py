#!/usr/bin/env python3

import pandas as pd
import os, scipy.stats
import numpy as np
from sklearn.preprocessing import Imputer
from sklearn.preprocessing import MaxAbsScaler

#http://scikit-learn.org/stable/modules/preprocessing.html#imputation-of-missing-values

def Impute():
    '''Imputes missing vals by mean, scales as sparse matrix'''
    info=pd.read_csv('/media/james/ext4data1/current/projects/pfizer/final_vecs.csv', encoding='utf-8')
    info=info.set_index('PATIENT')
    
    #tested axes- we want axis 0 to impute mean down a column
    imp = Imputer(missing_values='NaN', strategy='mean', axis=0)
    X= imp.fit_transform(info)
    
    #using a sparse data scaler due to the number of zeros from binarized variables
    mas= MaxAbsScaler()
    X= mas.fit_transform(X)
    
    #str((np.count_nonzero(X)/(X.shape[0]*X.shape[1]))*100) to get density... 96% sparse 
    #Should return to the psych scales (madrs, hamd etc) and encode using OneHotEncoder, since continuous variables are expected.
    
    np.savetxt('/media/james/ext4data1/current/projects/pfizer/data.csv', X, delimiter=',')
    
    return
