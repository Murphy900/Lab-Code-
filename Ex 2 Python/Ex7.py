'''
Write a Python library containing functions to perform the following operations for 
NumPy 1D arrays:

*Calculate the mean of its elements

*Calculate the variance of its elements

*Calculate the standard deviation of its elements

*Calculate the standard deviation from the mean of its elements
'''

import numpy as np

def mean(x):
    sum = np.sum(x)
    mu = sum/len(x)
    return mu

def var(x):
    variance = np.sum((x-mean(x))**2)/(len(x)-1)
    return variance

def Std(x):
    std = np.sqrt(var(x))
    return std

def stdmean(x):
    stdmu = Std(x)/np.sqrt(len(x))
    return stdmu

def main():
    x = np.array([1,2,3,4])
    print(mean(x))
    print(var(x))
    print(Std(x))
    print(stdmean(x))
    return

if __name__ == '__main__':
    main()
