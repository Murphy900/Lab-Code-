import matplotlib.pyplot as plt
import numpy as np
from math import sqrt
import random

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# generate a pseudo random number with uniform pdf in an interval [xmin,xmax]
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

def rand_range (xMin,xMax):
    return xMin + random.random() * (xMax-xMin)


# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
#This function generates N random numbers from a seed in an interval (xMin,xMax). The numbers follows a uniform distribution
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

def generate_range(xMin, xMax,N,seed = 0.):
     
     if seed != 0. : random.seed (float (seed)) #if seed is not a float number make a cast on it
     randlist = []
     #Generation of N random float numbers with values between xMin and xMax

     for i in range(0,N):
        randlist.append(xMin + random.random() * (xMax-xMin))
    
     return randlist

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# This method generate pseudo-random numbeers between 0 and 1 with uniform distribution initialized by a seed 
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -


def generate_uniform(N, seed = 0.):

    if seed != 0. : random.seed(float(seed))
    randlist = []
    for i in range (0,N):
        
        randlist.append(random.random())
    return randlist


#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
''' 
 generazione di un numero pseudo-casuale con il metodo del teorema centrale del limite note media e sigma della gaussiana
'''
#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
def rand_TCL_ms (mean, sigma, N_sum = 10) :
    
   
    y = 0.
    delta = sqrt (3 * N_sum) * sigma
    xMin = mean - delta
    xMax = mean + delta
    for i in range (N_sum) :
        y = y + rand_range (xMin, xMax)
    y /= N_sum ;
    return y ;


#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
''' 
    generazione di N numeri pseudo-casuali con il metodo del teorema centrale del limite, note media e sigma della gaussiana,
    a partire da un determinato seed
'''
#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

def generate_TCL_ms (mean, sigma, N, N_sum = 10, seed = 0.) :
   
    if seed != 0. : random.seed (float (seed))
    randlist = []
    delta = sqrt (3 * N_sum) * sigma
    xMin = mean - delta
    xMax = mean + delta
    for i in range (N):
        # Return the next random floating point number in the range 0.0 <= X < 1.0
        randlist.append (rand_TCL (xMin, xMax, N_sum))
    return randlist


# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# Generate pseduo-random numbers using Cenetral Limit Theorem 
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

def rand_TCL(xMin,xMax,N_sum = 10):
   
   y = 0.
   for i in range(N_sum):
      y = y + rand_range(xMin,xMax) #every time the function rand_TCL is called rand_range change value and produce a new average of 10 pseudo random numbers that follow a uniform distribution
   z = y/N_sum
   return z
   
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# this function generate N random numbers that follows a Gaussian Distribution when N get bigger 
# it was set N_sum = 10 for making sample set of ten pseudo random numbers to evaluate sample mean 
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

def generate_TCL(xMin,xMax,N, seed = 0.):

   if seed != 0. : random.seed(float(seed))
   randlist = []
   
   for j in range(N):
      
      randlist.append(rand_TCL(xMin,xMax))

   return randlist 

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# Generate pseduo-random numbers using Cenetral Limit Theorem for a pdf
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

def randTCL_pdf(pdf,xmin,xmax,ymax,N_sum = 10):
    y = 0.
    for i in range(N_sum):
       y = y + rand_TAC(pdf,xmin,xmax,ymax)[0] 
    z = y/N_sum
    return z

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# this function generate from a pdf  N random numbers that follows a Gaussian Distribution when N get bigger 
# it was set N_sum = 10 for making sample set of ten pseudo random numbers to evaluate sample mean 
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

def generateTCL_pdf(pdf,xmin,xmax,ymax,N_sum = 10,sample_size = 10,seed = 0.):

    if seed != 0. : random.seed(float(seed))
    randlist = []
   
    for j in range(N_sum):
      
      randlist.append(randTCL_pdf(pdf,xmin,xmax,ymax,sample_size))

    return randlist                     
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
#Generate a pseudo random number x that follows a pdf f. The method use the Try and Catch Algorithm
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    
def rand_TAC (f,xMin,xMax,yMax):

    x = rand_range(xMin,xMax)
    y = rand_range(0,yMax)
    counts = 0

    while (y>f(x)):
        
        x = rand_range(xMin,xMax)
        y = rand_range(0,yMax)
        counts += 1

    return x,counts

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
#This method generate using the algorithm Try and Catch a distribution of N pseudo-random numbers that follow the pdf f 
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

def generate_TAC (f,xMin,xMax,yMax,N,seed = .0):
    if seed != .0 : random.seed(float(seed))
    randlist = []
    counts = []

    for i in range (0,N):
        randlist.append(rand_TAC(f,xMin,xMax,yMax)[0])
        counts.append(rand_TAC(f,xMin,xMax,yMax)[1])

    return randlist,counts
    

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
#this method  generate a single event that follow an exponential pdf
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

def rand_exp(tau,seed = 0.):
     
     if tau <= 0. : raise ValueError('Tau must be a positive number')
     if seed != 0. : random.seed(float(seed))
     y = random.random()
     f = lambda y : -tau*np.log(1-y) # cumulative distribution function for an exponential pdf(x)
     return f(y)

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# This method generate N event that follow an exponential pdf
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

def generate_exp(tau,N,seed = 0.):
     exp = []
     if seed != 0. : random.seed(float(seed))
     for i in range(N): exp.append(rand_exp(tau,seed))
     return exp

# ---------------------------------------------------------------------------------------------------------------
#Generating a pseduo random number that follow Poisson Distribution from exponential pdf with lambda fixed at 1
#---------------------------------------------------------------------------------------------------------------

def rand_poisson(mean, tau = 1.):

    total_time = rand_exp(tau)
    events  = 0 
    while total_time < mean :
        events += 1
        total_time += rand_exp(tau)
    return events 

# ---------------------------------------------------------------------------------------------------------------
# this method generate a set of random numbers that follow the poisson pdf
#-----------------------------------------------------------------------------------------------------------------

def generate_poisson(mean,N,tau = 1.,seed = 0.):
    
    if seed != 0. : random.random(float(seed))
    randlist = []

    for i in range(N):
        randlist.append(rand_poisson(mean,tau))
    
    return randlist 