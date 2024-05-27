from inspect import isfunction
import numpy as np
import math
from numpy import abs

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#This algorithm find the bound extrema in which fall at least a zeros of the function f, starting from an interval in which no zeros are in it.
#It's an extension of the algorithm showed in the root finding section of numerical recipes book for c++. 
# Excluded the existence of at least a zero in the bracket [x1,x2] the algorithm perform a search outward the brackets finding the extrema in which at least a zero exist.
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def zoutward(n,x1,x2,f):
    
    if isfunction(f) != True :
        raise TypeError("f must be a function of one variable")
        
    if x1 > x2 :
        raise ValueError(str(x1) + ' must be lesser than ' + str(x2) + ' in an interval of the type [x1,x2]')

    dx = x2-x1/n # increment factor of the extrema of the bracket
    Ntry = 50 # number of try before the algorithm stops
    
    fp1 = f(x1)
    fp2 = f(x2)
    
    xb1 = [] # list of the bracket extrema where at least exist a zero moving to left of x1
    xb2 = [] # list of the bracket extrema where at least exist a zero moving to the right of x2

    for j in range (0,Ntry):
        x1 -= dx
        x2 += dx
        fc1 = f(x1)
        fc2 = f(x2)

        if fp1*fc1 <= 0.0:
            xb1.append(x1)
            xb1.append(x1+dx)

        if fp2*fc2 <= 0.0:
            xb2.append(x2-dx)
            xb2.append(x2) 
        
        fp1 = fc1
        fp2 = fc2
    
    if len(xb1) == 0 and len(xb2) == 0 :
        print('Function f doesn\'t have zeros out of the bracket [x1,x2]')
    else:
        return [xb1,xb2]

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# As the algorithm before this one search the zeros of a function but at diference of the other one it look inward the bracket [x1,x2].
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def zinward(n,x1,x2,f) : 

    if isfunction(f) != True :
        raise TypeError('f must be a one variable function')
        

    if x1 > x2 :
        raise ValueError(str(x1) + ' must be lesser than ' + str(x2) + ' in an interval of the type [x1,x2]')
        

    dx = (x2-x1)/n
    fp = f(x1)
    x = []
    

    while math.ceil(x1) != x2 :
        x1 += dx
        fc = f(x1)  

        if fc*fp <= 0.0 :
            x.append(x1-dx)
            x.append(x1)
        
        fp = fc
        
    if len(x) == 0:
       print('Function f doesn\'t have zeros inside the bracket [x1,x2]')
    else:
        return x


#------------------------------------------------------------------------------------------------------------------------------------------------
# This method implement the bisection algorithm to estimate the value of the zeros of the function.
# If there are more zeros in a bracket the method start to approximate the first zero that find in the interval
#------------------------------------------------------------------------------------------------------------------------------------------------


def bisection(x1,x2,f):

    if x1 > x2:
        raise ValueError(str(x1) + ' must be lesser than ' + str(x2) + ' in an interval of the type [x1,x2]')
    if f(x1)*f(x2) > 0.0 :
        raise ValueError('There aren\'t zeros in the bracket'+'['+ str(x1) + ',' + str(x2) + ']')
    
    
    eps = np.finfo(np.float64).eps # return double digits machine precision 
    xacc = eps*(abs(x2)+ abs(x1))/2 # defines the precision of the approximation of the zeros of the function
    dx = x2-x1

    while(dx > xacc):
        xmid = (x1+x2)/2
    
        if f(xmid)*f(x1) < 0 :
            x2 = xmid
        else:
            x1 = xmid

        if f(xmid) == 0:
            break
        dx = x2 - x1
    return xmid
