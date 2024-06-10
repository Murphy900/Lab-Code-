import numpy as np
from numpy import abs
from math import sqrt

R = 0.61803399 # Golden Ratios
C = 1.0 - R
PRECISION = sqrt(np.finfo(np.float64).eps) #return double digits machine precision 

# ----------------------------------------------------------------------------------------
#This method evaluate the minimum of a function using the golden ratio search algorithm
# ----------------------------------------------------------------------------------------

def goldenratioMin(f,xmin,xmax):
    
    len = abs(xmax - xmin)

    while len > PRECISION :
        
        x1 = xmin + R*(xmax - xmin)
        x2 = xmin + C*(xmax-xmin)
        
        if f(x2) > f(x1):
            xmin = x2
        else: 
            xmax = x1
        
        len = abs(xmax-xmin)
        
    if f(x1) <f(x2):
        return x1
    else: 
        return x2 
    
    #return (xmin + xmax)/2

# ----------------------------------------------------------------------------------------
#This method evaluate the maximum of a function using the golden ratio search algorithm
# ----------------------------------------------------------------------------------------
            
def goldenratioMax(f,xmin,xmax):

    len = abs(xmax - xmin)

    while len > PRECISION :
        
        x1 = xmin + R*(xmax - xmin)
        x2 = xmin + C*(xmax-xmin)
        
        if f(x2) < f(x1):
            xmin = x2
        else: 
            xmax = x1
        
        len = abs(xmax-xmin)
        
    if f(x1) < f(x2):
        return x1
    else: 
        return x2 