'''
Read the text file eventi_gauss.txt:

*Fill a histogram with the first N numbers contained in the file,
 where N is a command-line parameter during program execution.

*Choose the histogram’s definition range and its bin number based 
on the numbers to be represented.

'''

import sys
import numpy as np
import matplotlib.pyplot as plt
from Ex1 import sturges

def openFile():
    with open(sys.argv[1]) as input_file:
        sample = [float(x) for x in input_file.readlines()]
    return sample

def main():

    sample = openFile() 
    filter  = int(input('Inserisci  il numero di dati da leggere: ' ))

    N_bins = sturges(filter)
    bin_edges = np.linspace(np.min(sample),np.max(sample),N_bins)
    fig, ax = plt.subplots(1,1)
    ax.hist(sample, color = 'orange',bins = bin_edges)
    plt.show()

    return

if __name__ == '__main__':
    main()
