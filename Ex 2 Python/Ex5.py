'''
*After finding how the numpy.sort function works, write a Python library 
containing a function that determines the median of an array.

*Write a main program that tests the performance of the developed function.

'''
import numpy as np
import sys

def mean(x):
    y = np.array(x)
    sorted = np.sort(y)
    mean = np.mean(sorted)
    return mean

def main (): 
    x = []
    for i in range(3,len(sys.argv)):
        x.append(int(sys.argv[i]))
    print(sys.argv[3])
    print(x)
    
    media = mean(x)
    print('the mean is: ' + str(media))
    return

if __name__ == '__main__':
    main()