'''
*Given an array of numbers, write a Python library containing a function which 
determines the value below which lies the 25% of the values, and the one 
above which lies the 25% of the the values

*Generalise the function to the case where the percentage of tails is set 
as input value

'''

import numpy as np

def quantile(x,p):
    
    sorted = np.sort(x)
    q1 = 0
    q3 = 0
    if p > 1 and p>0:
        below = p/100
        above = 1 - below
        q1 = len(x)*below
        q3 = len(x)*above
    else:
        above = 1-below
        q1 = len(x)*p
        q3 = len(x)*above
    
    #check for fist quantile
    if np.abs(q1-int(q1)) == 0: 
        q1 = int(q1)
        q1 = (2*q1+1)/2
    else:
        q1 = int(q1)+1
    
    #check for greater quantile
    if np.abs(q3-int(q3)) == 0: 
        q3 = int(q3)
        q3 = (2*q3+1)/2
    else:
        q3 = int(q3)+1
    

    return [q1,q3]

def main():
    x = np.array(list(range(1,11)))
    print(x)
    quant = quantile(x,25)
    print(quant)
    return 

if __name__ == '__main__':
    main()