'''
*Create a one-dimentional NumPy array containing a sequence of integer 
numbers from 1 to 100

*Starting from this, create a one-dimensional NumPy array containing in each 
entry the sum of integer numbers from 1 until the index of that entry

'''
import numpy as np

#Question 1

numbers = list(range(1,101))
integer_list = np.array(numbers)
print(integer_list)

#Question 2

sum = np.zeros(len(numbers))

for i in range (0,len(numbers)):
    if i == 0 : sum[i] = integer_list[i]
    else:
        temp=np.zeros(i+1)
        for j in range(0,i+1):
            temp[j] = integer_list[j]
            #print(temp)
        sum[i] = np.sum(temp)

print(sum)
