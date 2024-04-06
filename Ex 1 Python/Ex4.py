#Write a program that, by using a for loop, returns the Fibonacci sequence up to the n-th term and stores it in a python dictionary, 
#where the key represents the index of each element and value its actual value.
import sys

def Fibonacci1(n):
    i=0
    fib = {0:0, 1:1}
    if n == 0:
        return {0:0}
    else:
        for i in range (0,n-1):
            z = fib[i+1] + fib[i]
            fib[i+2] = z
    return fib 

def main():
    n_grade = int(sys.argv[1])
    print(Fibonacci1(n_grade))
    return 
    
# ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- 

if __name__ == '__main__' :
    main()