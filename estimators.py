#!/usr/bin/env python3

import numpy as np
import copy, pickle
from sklearn import svm, naive_bayes, neighbors, ensemble, linear_model, tree, discriminant_analysis

def Highlander():
    with open('/media/james/ext4data1/current/projects/pfizer/vectors/inner_cv.pickle','rb') as f: 
        cv=pickle.load(f)       
    
    scores={'fold': [], 'train':[], 'test':[]}

    for i in range(10):  
        X_train=cv['X_train'][i]
        X_test=cv['X_test'][i]
        
        y_train= cv['y_train'][i]
        y_test= cv['y_test'][i]

        #est= ensemble.RandomForestClassifier()
        #est= ensemble.ExtraTreesClassifier()
        #est= neighbors.KNeighborsClassifier()
        est= naive_bayes.GaussianNB()
        #est= tree.DecisionTreeClassifier()
        #est= svm.LinearSVC()
        #est= discriminant_analysis.LinearDiscriminantAnalysis()
        
        est.fit(X_train, y_train)
                
        print('\nFold {}/10\n'.format((i+1)))
        
        predicted_train= est.predict(X_train)
        train_score= est.score(X_train, y_train)
        print('X_train predictions: {}'.format(predicted_train))
        print('y_train actual vals: {}'.format(y_train))        
        print('Training set score: {}%\n'.format((train_score*100)))
        
        predicted_test= est.predict(X_test)
        test_score= est.score(X_test, y_test)
        print('X_test predictions: {}'.format(predicted_test))
        print('y_test actual vals: {}'.format(y_test))
        print('Baseline accuracy: {}'.format('50%'))
        print('Test set score: {}%\n'.format((test_score*100)))

        scores['fold'].append(i)
        scores['train'].append(train_score)
        scores['test'].append(test_score)
                
    print('All Train Average Acc: {}%'.format((sum(scores['train'])/10)*100))
    print('All Test Average Acc: {}%'.format((sum(scores['test'])/10)*100))
    print('All Test Expected Acc: 50%')
    print('Combined acc per outer fold:\n{}'.format(np.add.reduceat(scores['test'], np.arange(0, 10, 2))*100/2))    
        
    with open('/media/james/ext4data1/current/projects/pfizer/vectors/est_scores.pickle', 'wb') as d: pickle.dump(scores, d, pickle.HIGHEST_PROTOCOL) 

    return
    
def Quickening():
    with open('/media/james/ext4data1/current/projects/pfizer/vectors/inner_cv.pickle','rb') as f: 
        cv=pickle.load(f)       
    
    scores={'fold': [], 'train':[], 'test':[]}
    
    for i in range(5):
        X_train=cv['X_train'][i]
        X_test=cv['X_test'][i]
        
        y_train= cv['y_train'][i]
        y_test= cv['y_test'][i]
        
        #est= ensemble.RandomForestClassifier()
        #est= ensemble.ExtraTreesClassifier()
        #est= neighbors.KNeighborsClassifier()
        est= naive_bayes.GaussianNB()
        #est= tree.DecisionTreeClassifier()
        #est= svm.LinearSVC()
        #est= discriminant_analysis.LinearDiscriminantAnalysis()
        
        est.fit(X_train, y_train)
                
        print('\nFold {}/5\n'.format((i+1)))
        
        predicted_train= est.predict(X_train)
        train_score= est.score(X_train, y_train)
        print('X_train predictions: {}'.format(predicted_train))
        print('y_train actual vals: {}'.format(y_train))        
        print('Training set score: {}%\n'.format((train_score*100)))
        
        predicted_test= est.predict(X_test)
        test_score= est.score(X_test, y_test)
        print('X_test predictions: {}'.format(predicted_test))
        print('y_test actual vals: {}'.format(y_test))
        print('Baseline accuracy: {}'.format('50%'))
        print('Test set score: {}%\n'.format((test_score*100)))

        scores['fold'].append(i)
        scores['train'].append(train_score)
        scores['test'].append(test_score)
                
    print('All Train Average Acc: {}%'.format((sum(scores['train'])/5)*100))
    print('All Test Average Acc: {}%'.format((sum(scores['test'])/5)*100))
    print('All Test Expected Acc: 50%')
    print('Combined acc per outer fold:\n{}'.format(np.add.reduceat(scores['test'], np.arange(0, 5, 1))*100))    
        
    with open('/media/james/ext4data1/current/projects/ramasubbu/est_scores.pickle', 'wb') as d: pickle.dump(scores, d, pickle.HIGHEST_PROTOCOL) 

    return
