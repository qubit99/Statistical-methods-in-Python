import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from math import pi,e

def findmean(arr,l):
    return sum(arr)/l


def findsd(arr,l,mean):
    s=0
    for i in range(l):
       s+=(arr[i]-mean)**2
    return (s/(l-1))**(0.5)


def proabilitydensityfunc(x,mu,sigma):

    f = (1/(sigma)*((2*pi)**(0.5))) * e**(-((x-mu)**2)/(2*(sigma**2)))
    return f

if __name__=='__main__':
    data=pd.read_csv('StudentsPerformance.csv',sep=',',header=0)
    data=data.dropna()
    X=data['math score']  #trying other columns gave similar results
    x=list(X)
    length=len(x)
    mu = findmean(x,length)
    sigma = findsd(x,length,mu)
    x=np.linspace(mu-5*sigma,mu+5*sigma,50)
    y=proabilitydensityfunc(x,mu,sigma)
    plt.plot(x,y,'r')
    plt.show()
    a=int(input("Enter marks to calculate it's maximum liklelihood estimate "))
    b=proabilitydensityfunc(a,mu,sigma)
    print("Maximum likelihood estimate is",b)
