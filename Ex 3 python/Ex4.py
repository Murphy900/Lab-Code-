'''
*Display the distributions of events from the two files of the previous exercises, 
overlaid, finding the best visualization for the comparison between the two histograms.

'''

import sys
import numpy as np
from Ex1 import sturges
from Ex3 import openFile
import matplotlib.pyplot as plt

def main():

    sample1 = []
    sample2 = []
    
    with open(sys.argv[1]) as input_file:
        sample1 = [float(x) for x in input_file.readlines()]

    with open(sys.argv[2]) as input_file:
        sample2 = [float(x) for x in input_file.readlines()]
    
    print('Dataset 1 dimension: ', len(sample1))
    print('Dataset 2 dimension: ', len(sample2))

    N_bins = sturges(len(sample1))
    

    print('max sample1: ',np.max(sample1),'max sample2 : ',np.max(sample2))
    print('min sample1: ',np.min(sample1),'min sample2: ', np.min(sample2))

    bin_edges2 = np.linspace(np.min(sample2),np.max(sample2),N_bins)
    bin_edges1 = np.linspace(np.min(sample1),np.max(sample1),N_bins)
    fig, ax = plt.subplots(1,1)

    ax.hist(sample1, color = 'orange',bins = bin_edges1)
    ax.hist(sample2, color = 'blue',bins = bin_edges2, alpha = 0.5)
    plt.show()
    
    return



if __name__ == '__main__':
    main()
