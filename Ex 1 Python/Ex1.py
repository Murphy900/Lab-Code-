import sys

def CommonDivCheck(n,m):
    if n>m :
        residual = n % m
        if residual != 0 :
            print('the remainder of  is: ' + str(residual) + ' and {0} is not divisible for {1}'.format(n,m))
        else:
            print('{0} is divisible for {1} and the remainder is: '.format(n,m)+ str(residual))
    else:
        print('I can\'t perform the operation of integer division if {0} < {1}'.format(n,m))


def main():
    n1  = int(sys.argv[1])
    n2  = int(sys.argv[2])
    CommonDivCheck(n1,n2)
    return

#------------------------------------------------------------
#if the script is runnig as a program python asign the name as main and the function main is executed
# else if the script is imported as a module the name != main and the main function is not executed 
# this practice is usefull for debugging reason of the single script 

if __name__ == "__main__":
    main()