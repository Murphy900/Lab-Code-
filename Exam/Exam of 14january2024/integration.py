
from myrand import generate_range
import stats
from math import sqrt



#--------------------------------------------------------------------------------------------------------
#This method calculate the integral of a function using the algorithm hit or miss and the error
#of the estimate value.
#--------------------------------------------------------------------------------------------------------

def integral_HOM (func, xMin, xMax, yMax, N_evt,seed = 0.) :

    x_coord = generate_range (xMin, xMax,N_evt,seed)
    y_coord = generate_range (0., yMax,N_evt,seed)

    points_under = 0
    for x, y in zip (x_coord, y_coord): #zip () generate a list of couple 
        if (func(x) > y) : points_under = points_under + 1 

    A_rett = (xMax - xMin) * yMax
    frac = float (points_under) / float (N_evt)
    integral = A_rett * frac
    integral_unc = A_rett**2 * frac * (1 - frac) / N_evt
    
    return integral, integral_unc


#------------------------------------------------------------------------------------------------------------------------------------------
# This method implement a simple Monte Carlo algorithm for the evalutation of a one variable integral
#------------------------------------------------------------------------------------------------------------------------------------------

def simple_MonteCarlo(f, xMin,xMax, N_event):
    
    x_coord = generate_range(N_event,xMin,xMax)

    range = (xMax - xMin)
    f_list = [f(x) for x in x_coord]
    f_mean = stats(f_list).mean()
    integralValue = f_mean*range
    f_square = [f(x)*f(x) for x in x_coord]
    integralError = range*sqrt((stats(f_square).mean() - f_mean*f_mean)/len(f_list))
    
    return [integralValue,integralError]
