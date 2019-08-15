import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import random
import time
from math import pi,e


def findmean(arr,l):
    return sum(arr)/l


if __name__=='__main__':
    data=pd.read_csv('StudentsPerformance.csv',sep=',',header=0)
    
    data=data.dropna()
    X=data['math score']  #trying other columns gave similar results
    x=list(X)
    plt.ion()
   
     
    for length in range(1000,20,-1):
        means=[]
        for i in range(200):
            arr=random.sample(x,length)
            mean=findmean(arr,length)
            means.append(mean)
    
        plt.hist(means, bins=100)
        
        plt.draw()
        plt.pause(0.2)
        plt.clf()
        
    plt.ioff()
    plt.show()
    
        
