'''
* Create a one-dimensional histogram filled with 5 values and save 
the histogram image to a png file
'''

import matplotlib.pyplot as plt
import numpy as np
from math import ceil 

# stugrges take as input an interger as the lenght of the sample

def sturges(N_events):
    return ceil(1+3.322 * np.log(N_events))

def main():
    rng = np.random.default_rng()
    sample = rng.standard_normal(10)
    print(sample)


    N_bins = sturges(len(sample))
    bin_edges = np.linspace(np.min(sample),np.max(sample), N_bins)

    fig, ax  = plt.subplots(nrows=1 , ncols= 1)
    ax.hist (sample,color='orange',bins = bin_edges)
    plt.savefig('Sample Distribution.png')
    plt.show()
    return

if __name__ == '__main__':
    main()