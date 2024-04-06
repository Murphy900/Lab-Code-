'''
Write a python library which, given the name of a text file containing a sample of events as input, 
is able to read the sample and save it in a numpy array, then calculate its mean, variance, 
standard deviation, standard deviation from the mean, display the sample in a histogram with an 
appropriately chosen definition range and bin number. Write a test program for the created library.
'''
import sys
import numpy as np
from math import ceil
import matplotlib.pyplot as plt


def openFile():
    with open(sys.argv[1]) as input_file:
        sample = [float(x) for x in input_file.readlines()]
        sample = np.array(sample)
    return sample

def sturges(N_events):
    return ceil(1+3.322 * np.log(N_events))

def momenta(sample):
    sampleMean = np.mean(sample)
    sampleVar = np.var(sample)
    sampleStd = np.sqrt(sampleVar)
    sampleMeanStd = sampleStd/np.sqrt(len(sample))

    print(' Mean: ', sampleMean, '\n' ,'Variance: ', sampleVar, '\n', 
          'Standard Deviation: ', sampleStd, '\n','Std from mean: ', sampleMeanStd )
    return [sampleMean,sampleVar,sampleStd,sampleMeanStd]

def Histogram(sample):
    
    N_bins = sturges(len(sample))
    bin_edges = np.linspace(np.min(sample),np.max(sample),N_bins)
    fig,ax  = plt.subplots(1,1)
    ax.hist(sample,color = 'blue', alpha = 0.5, bins = bin_edges)
    plt.show()

    return


def main():
    sample = openFile()
    moment = momenta(sample)
    Histogram(sample)


    return
if __name__ == '__main__':
    main()
