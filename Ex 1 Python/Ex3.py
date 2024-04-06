#Write a program that, by using a while loop, returns the Fibonacci sequence 
#up to the n-th term and stores it in a python list.
import sys

#Function return a list of fibonacci number until n-grade asked 

def Fibonacci(n):
    if n == 0:
        return 0
    else:
        counter = 0
        list = [0,1]
        while counter != n-1:
            z = list[counter + 1] + list[counter]
            list.append(z)
            counter += 1
    return list

def main():
    n_grade = int(sys.argv[1])
    print(Fibonacci(n_grade))
    return 
# ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- 

if __name__ == '__main__' :
    main()