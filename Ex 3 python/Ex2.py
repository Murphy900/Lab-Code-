'''
Read the text file eventi_unif.txt:

*Print the first 10 positive elements to the screen.

*Count the number of events contained in the file. (it could mean count the number of line ?

*Determine the minimum and maximum values among the numbers saved in the file.

'''
import sys 
import numpy as np

def main():

    with open(sys.argv[1]) as input_file:
        
        sample = [float(x) for x in input_file.readlines()]
        

        positive = np.zeros(10)

        for x in sample:
            if x > 0:
                for i in range(0,10):
                    positive[i] = x
    
        xMax = np.max(sample)
        xMin = np.min(sample)
    print(positive)
    print('Maximum of sample is: ' , xMax, ' and Minimum of sample is: ', xMin)

    with open(sys.argv[1]) as input_file:
        numberLines = len(input_file.readlines())

    print('Total Number of lines:', numberLines)
    
    return


if __name__ == '__main__':
    main()