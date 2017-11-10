#!/usr/bin/env python3

from sklearn.feature_selection import SelectKBest
import copy, pickle
import numpy as np

#Run feature selection. Data here need to be transformed because they'll be used in the ML step.

def InnerFeats():
    with open('/media/james/ext4data1/current/projects/pfizer/icv.pickle','rb') as f: icv=pickle.load(f)       
    X_train= icv['X_train']
    X_test= icv['X_test']
    y_train= icv['y_train']
    y_test= icv['y_test']
    train_indices= icv['train_indices']
    test_indices= icv['test_indices']
    
    folds= len(icv['X_train'])
    feats=[[0]]*folds
    
    for i in range(folds):
        subjects=len(X_train[i])
        skb= SelectKBest(k=subjects)
        skb.fit(X_train[i], y_train[i])
        feats[i]=skb.get_support(indices=True)
        X_train_feats= skb.transform(X_train[i])
        X_test_feats= skb.transform(X_test[i])
        X_train[i]= np.array(X_train_feats)
        X_test[i]= np.array(X_test_feats)
    
    featdict={'Feature Indices':feats, 'X_train':X_train, 'X_test':X_test, 'y_train':y_train, 'y_test':y_test, 'train_indices':train_indices, 'test_indices':test_indices}
        
    with open('/media/james/ext4data1/current/projects/pfizer/icvfeats.pickle','wb') as f: pickle.dump(featdict, f, pickle.HIGHEST_PROTOCOL)
        
    return    

def OuterFeats():
    with open('/media/james/ext4data1/current/projects/pfizer/ocv.pickle','rb') as f: ocv=pickle.load(f)       
    X_train= ocv['X_train']
    X_test= ocv['X_test']
    y_train= ocv['y_train']
    y_test= ocv['y_test']
    train_indices= ocv['train_indices']
    test_indices= ocv['test_indices']
    
    folds= len(ocv['X_train'])
    feats=[[0]]*folds
    
    for i in range(folds):
        subjects=len(X_train[i])
        skb= SelectKBest(k=subjects)
        skb.fit(X_train[i], y_train[i])
        feats[i]=skb.get_support(indices=True)
        X_train_feats= skb.transform(X_train[i])
        X_test_feats= skb.transform(X_test[i])
        X_train[i]= np.array(X_train_feats)
        X_test[i]= np.array(X_test_feats)
    
    featdict={'Feature Indices':feats, 'X_train':X_train, 'X_test':X_test, 'y_train':y_train, 'y_test':y_test, 'train_indices':train_indices, 'test_indices':test_indices}
        
    with open('/media/james/ext4data1/current/projects/pfizer/ocvfeats.pickle','wb') as f: pickle.dump(featdict, f, pickle.HIGHEST_PROTOCOL)
        
    return
