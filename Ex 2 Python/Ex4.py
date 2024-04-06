'''
Inside a Python program, the current time may be obtained with the 
time library

*Compare the time performances of element-wise operations 
performed between two lists with respect to the same operation 
performed in compact form between two NumPy arrays

*After which size the differences start being significant? 

Observing the plot of time in function of list or array dimension show 
that numpy array are more efficiet for every dimension in doing algebric 
operation of element wise sum between array than the python list.

'''

import numpy as np
import time as t
import matplotlib.pyplot as plt

computation_time_numpy = []
computation_time_list = []
number = [10,100,1000,10000,100000,1000000,10000000]

for n in number:
    n1 = np.array(list(range(0,n)))
    n2 = np.array(list(range(0,n)))
    sum = n1+n2
    computation_time_numpy.append(t.time())

for n in number:
    n1 = list(range(0,n))
    n2 = list(range(0,n))
    sum = []
    
    for j in range(0,len(n1)):
        sum.append(n1[j] + n2[j])
    computation_time_list.append(t.time())
    
    

ctl = np.array(computation_time_list)
ctn = np.array(computation_time_numpy)
x = np.array(number)


plt.plot(x,ctl, label = 'Somma liste')
plt.plot(x,ctn, label = 'Somma numpy array')
plt.xlabel('Dimensione')
plt.ylabel('Tempo Operazione Somma')
plt.legend()
plt.show()

