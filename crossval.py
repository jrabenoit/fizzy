#!/usr/bin/env python3

import pprint, itertools, pickle
import numpy as np
from collections import defaultdict
from sklearn.feature_selection import SelectKBest
from sklearn.model_selection import StratifiedKFold

def OuterCv():   
    
    data=np.loadtxt('/media/james/ext4data1/current/projects/pfizer/ready.csv', delimiter=',')
    labels=pd.read_csv('/media/james/ext4data1/current/projects/pfizer/labels_placebo.csv', encoding='utf-8')
    labels= list(labels['GROUPLABEL'])
        
    print('Treatment Response: 379 subjects, 200 remitters (52.77%), 179 with HAM-D > 7\n')
    
    group0=group0.ix[:,5:25]
    group1=group1.ix[:,5:25]
    
    outer_cv={'X_train': [], 'X_test': [],
              'y_train': [], 'y_test': []}

    X= pd.DataFrame.append(group0,group1)
    y= labels
    
    X_train, X_test, y_train, y_test= [], [], [], []      

    print('\nGroup size: {}, 0: {}, 1: {}'.format(len(X), len(group0), len(group1)))
    print('Label size: {}\n'.format(len(y)))

    skf = StratifiedKFold(n_splits=5)
    for train_index, test_index in skf.split(X,y):
        X_train, X_test= X.ix[train_index], X.ix[test_index]
        y_train, y_test= y[train_index], y[test_index]       
    
        outer_cv['X_train'].append(X_train)
        outer_cv['X_test'].append(X_test)
        outer_cv['y_train'].append(y_train)
        outer_cv['y_test'].append(y_test)
    
    with open('/media/james/ext4data1/current/projects/pfizer/vectors/outer_cv.pickle', 'wb') as f: pickle.dump(outer_cv, f, pickle.HIGHEST_PROTOCOL) 

    return
    
def InnerCv():
    '''Set up as a flat structure of 10 df'''
    with open('/media/james/ext4data1/current/projects/pfizer/vectors/outer_cv.pickle', 'rb') as f: outer_cv= pickle.load(f)

    inner_cv={'X_train': [], 'X_test': [],
              'y_train': [], 'y_test': []}
    
    X= outer_cv['X_train']
    y= outer_cv['y_train']
    
    X_train, X_test, y_train, y_test = [], [], [], []
    
    #change X to subjects, y to labels
    #read loop as, "for each pair of X and y lists in (X,y)"
    
    for X_, y_ in zip(X, y): 
        skf = StratifiedKFold(n_splits=2)
        for train_index, test_index in skf.split(X_,y_):      
            X_train, X_test= X_.ix[train_index], X_.ix[test_index]
            y_train, y_test= y_[train_index], y_[test_index]

            inner_cv['X_train'].append(X_train)
            inner_cv['X_test'].append(X_test)
            inner_cv['y_train'].append(y_train)
            inner_cv['y_test'].append(y_test)

    with open('/media/james/ext4data1/current/projects/pfizer/vectors/inner_cv.pickle', 'wb') as f:
        pickle.dump(inner_cv, f, pickle.HIGHEST_PROTOCOL) 
    
    return

    
