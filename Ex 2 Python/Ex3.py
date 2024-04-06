'''
*Create a one-dimensional array containing the sequence 
of the first 50 even natural numbers

*Create a one-dimensional array containing the sequence 
of the first 50 odd natural numbers

*Create a one-dimensional array containing the element-wise sum 
of the previous two arrays

'''

import numpy as np
numbers = np.array(list(range(1,101)))

odd = []
even = []

for i in range (0,len(numbers)):
    if numbers[i] % 2 == 0 :
        odd.append(numbers[i])
    else:
        even.append(numbers[i])
odd_array = np.array(odd)
even_array = np.array(even)

print('Array containing odd element :')
print(odd_array)

print('Array containing even element: ')
print(even_array)

sum = odd_array + even_array

print('Element wise sum array of odd and even numbers: ')
print(sum)