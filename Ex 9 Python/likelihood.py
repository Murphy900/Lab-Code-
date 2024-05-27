from math import prod,log

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

def loglikelihood(pdf,theta, sample):
    
    loglike = 0 

    for x in sample:
        if pdf(x,theta) > 0.: loglike += log(pdf(x,theta))
    
    return loglike