import sys

#Function angle check verify if the triangle is obtused, acuted or rectangular.
def anglecheck(a,b,c):
    list = [a,b,c]
    list.sort()
    print(list)
    if a+b+c == 180 :
        if list[2] > 90:
                print ('The triangle is obtused-angled ')
                return
        elif list[1] < 90 : 
            if list[2] == 90:               
                print('The triangle is rectangular-angled')
                return 
            else:    
                print('The triangle is acuted-angled')
                return
    else:
        print('A triangle need to have the sum of the angle equal to 180')
        return

def main():

    a = float(sys.argv[1])
    b = float(sys.argv[2])
    c = float(sys.argv[3])
    
    anglecheck(a,b,c)
    return

# ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- 

if __name__ == '__main__' :
    main()