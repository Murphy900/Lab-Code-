'''
Read the text file eventi_unif.txt:

Calculate the mean of the numbers in the text file.

Calculate the variance of the numbers in the text file.

Calculate the standard deviation of the numbers in the text file.

Calculate the standard deviation from the mean of the numbers in the text file.

'''

import sys
import numpy as np
from Ex3 import openFile
from Ex1 import sturges


def main():
    sample = openFile()

    sampleMean = np.mean(sample)
    sampleVar = np.var(sample)
    sampleStd = np.sqrt(sampleVar)
    sampleMeanStd = sampleStd/np.sqrt(len(sample)) 

    print(' Mean: ', sampleMean, '\n' ,'Variance: ', sampleVar, '\n', 
          'Standard Deviation: ', sampleStd, '\n','Std from mean: ', sampleMeanStd )
      
    return 

if __name__ == '__main__':
    main()
