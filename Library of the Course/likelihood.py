from math import log
import bisection as bs
from goldensearch import goldenratioMax

#--------------------------------------------------------------------
# This method calculate the likelihood of a parameter theta 
#--------------------------------------------------------------------

def likelihood(pdf,theta,sample):
    result = 1
    for x in sample:
        result *= pdf(x,theta)
    
    return result


#--------------------------------------------------------------------
# This method calculate the loglikelihood of a parameter theta 
#--------------------------------------------------------------------

def loglikelihood(pdf,theta,sample):
    
    loglike = 0 

    for x in sample:
        if pdf(x,theta) > 0.: loglike += log(pdf(x,theta))
    
    return loglike

#--------------------------------------------------------------------------------------------------------------
# this method calculate the loglikelihood ratio and return a list of the esteemed value 
#--------------------------------------------------------------------------------------------------------------

def LLR(pdf,theta,sample,xmin,xmax):

    L = []
    tau_hat= LEP(loglikelihood,pdf,sample,xmin,xmax)
    lmax = loglikelihood(pdf,tau_hat,sample)

    for x in theta:
        g = lambda x : loglikelihood(pdf,x,sample) - lmax
        L.append(g(x))
    
    return L

#--------------------------------------------------------------------------------------------------------------
#This method apply the Rao Cramer theorem for the esteem of the point at one standard deviation from the mean
#--------------------------------------------------------------------------------------------------------------

def RaoCramer(g, # likelihood function 
              pdf, # probabolity distribution of the sample
              sample, # sample of the data 
              theta, # parameter of the likelihood function
              xmin, # minimum of the interval
              xmax #maximum of the interval
              ):
    
    theta_hat = LEP(g,pdf,sample,xmin,xmax)
    Lmax = Ltheta(g,theta_hat,sample,pdf)
    
    L = lambda theta: Ltheta(g,theta,sample,pdf) - Lmax + 0.5 # Applying theorem of Rao-Cramer

    zeros = bs.zinward(1000,xmin,xmax,L) #ziward algorithm search inside the bracke [xmin,xmax] for the zeros of the function
                                      # and return a list of the interval in which the zeors are contained 
     
    taus_minus_sigma = bs.bisection(zeros[0][0],zeros[0][1],L)
    tau_plus_sigma = bs.bisection(zeros[1][0],zeros[1][1],L)

    return [taus_minus_sigma,tau_plus_sigma]

#------------------------------------------------------------------------
#this method make the likelihood method a funcion of the parameter theta 
#------------------------------------------------------------------------
def Ltheta(L,theta,sample,pdf):

    ltheta = lambda theta : L(pdf,theta,sample)
    
    return ltheta(theta)

#-----------------------------------------------------------------------------
# This Method calculate the maximum likelihood of a parameter theta
#-----------------------------------------------------------------------------
 
def LEP(L #likelihood or loglikelihood kind of function in function of theta parameter 
        ,pdf # probability distribution function that the sample follow
        ,sample # random generate measurement from the sample 
        ,xmin # minimum of the interval where to search the maximum of ltheta 
        ,xmax # maximum of the interval where to search the maximum of ltheta
        ):
     
    Ltheta = lambda theta : L(pdf,theta,sample)
    return goldenratioMax(Ltheta,xmin,xmax)