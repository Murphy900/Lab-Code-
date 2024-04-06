
#Define a function that returns the Fibonacci sequence up to the n-th term. ---- Check 1.3 exercise
#Test the function with a main program, filling a list with the elements of the sequence. ------ Check 1.3 exercise
#Create a new list containing only the elements with even index in the list.
#Create a new list containing only the elements with odd index in the list.
#Move the function in a library and import it in the main program. --- Check 1.3 exercise

from Ex3 import Fibonacci as FB

print("insert Fibonacci Sequence grade: ")
n = int(input())
fib = FB(n)

print(fib)

evenFibList = []
oddFibList = []

for x in range (0,len(fib)):
    if x % 2 == 0:
        evenFibList.append(fib[x])
    else:
        oddFibList.append(fib[x])

print('Fibonacci Sequence with even index: ')
print(evenFibList)
print('Fibonacci Sequence with odd index:')
print(oddFibList)