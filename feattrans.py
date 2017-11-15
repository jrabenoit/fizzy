#!/usr/bin/env python3


from sklearn.decomposition import PCA
import copy, pickle
import numpy as np

#Run feature selection. Data here need to be transformed because they'll be used in the ML step.

def InnerTrans():
    with open('/media/james/ext4data1/current/projects/pfizer/icvfeats.pickle','rb') as f: icv=pickle.load(f)       
    X_train= icv['X_train']
    X_test= icv['X_test']
    y_train= icv['y_train']
    y_test= icv['y_test']
    train_indices= icv['train_indices']
    test_indices= icv['test_indices']
    
    folds= len(icv['X_train'])
    feats=[[0]]*folds
    
    pca=PCA(n_components=15, whiten=True)
    #n_components is maxed according to the warning
    
    for i in range(folds):
        print(i+1)
        subjects=len(X_train[i])
        pca.fit(X_train[i], y_train[i])
        X_train_feats= pca.transform(X_train[i])
        X_test_feats= pca.transform(X_test[i])
        X_train[i]= np.array(X_train_feats)
        X_test[i]= np.array(X_test_feats)
    
    featdict={'Feature Indices':feats, 'X_train':X_train, 'X_test':X_test, 'y_train':y_train, 'y_test':y_test, 'train_indices':train_indices, 'test_indices':test_indices}
        
    with open('/media/james/ext4data1/current/projects/pfizer/icvfeats.pickle','wb') as f: pickle.dump(featdict, f, pickle.HIGHEST_PROTOCOL)
        
    return   
