#!/usr/bin/env python3

import os
import crossval, features, estimators, estpicker, bootstrap

def Pop():

    groups=[]
    runs=10

    for group in groups:
        run=1
        for i in range(runs):    
            print('BEGINNING RUN {}/{}'.format(run, runs))
            prep.Cutter()
            prep.Framer()
            crossval.OuterCV(group)
            crossval.InnerCV()    
            features.SelKBest()
            features.SelKBestOuter()
            estimators.InnerFolds(group, run)
            bestest= estpicker.Best(group, run)
            estimators.OuterFolds(group, run, bestest)
            bootstrap.Bill(group, run)
            run= run + 1
            print('RUN COMPLETE')    

    os.system('spd-say -r -50 -p -50 -t female3 "your groups have finished running. To run more groups, you must construct additional pylons."')
    
    return

