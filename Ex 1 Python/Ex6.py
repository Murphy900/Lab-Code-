
'''Write a python program that determines the solution of second-order equations'''


# list order have to be from the coefficient associated to the maximum grade of the polinomial to minimum 
def root(coef):
    if len(coef) == 3 and coef[0] != 0:
        solution = []
        delta = coef[1]**2 -4*coef[0]*coef[2]
        
        if delta > 0:
            r1 = (-coef[1] + delta**0.5)/(2*coef[0])
            solution.append(r1)
            r2 = (-coef[1] - delta**0.5)/(2*coef[0])
            solution.append(r2)
            return solution
        
        elif delta == 0:
            r1 = - coef[1]/(2*coef[0])
            return r1
        
        else:
            print('For a discriminant < 0 doesn \' t  exist solution that belong to the real line')
            return None
            
    
    elif len(coef) == 2:
        solution = []
        if coef[0] == 0:
            print('coef can not be 0')
        
        else: 
            r1 = 0
            solution.append(r1)
            r2 = - coef[1]/coef[0]
            solution.append(r2)
            return solution
        
    elif len(coef) == 1:
        return float(0)
    
    else:
        print('Insert a coeffcient vecotr greater than 0')

def inputcoef(n):
    
    coef=[]
    for i in range (0,n):
        ele = int(input())
        coef.append(ele)
    if len(coef) == 2:
        print('polynomial inserted is {0}x**2 + {1}x'.format(coef[0],coef[1]))
    elif len(coef) == 3:
        print('polynomial inserted is {0}x**2 + {1}x + {2}'.format(coef[0],coef[1],coef[2]))
    else:
        print('polynomial inserted is {0}x**2'.format(coef[0]))
    return coef
    

def main():

    n = int(input("Enter number of elements : "))
    coef = inputcoef(n)
    solution = root(coef)
    
    if type(solution) ==  float :
        print('The roots of the polynomial are x1 = ' + str(solution))
        
    elif solution == None:
        return 
    else:
        print('The roots of the polynomial are x1 = ' + str(solution[0]) + ' x2 = ' + str(solution[1]))
    return


# ----- ------- ------- -------- -------- --------- ---------- --------- --------- ---------- --------- ----------- ------- ---------- ---------

if __name__ == '__main__':
    main()
