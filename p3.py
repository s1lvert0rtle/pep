import math

if __name__=='__main__':
    num = 600851475143
    i=2
    while(i<=num):
        if(num%i==0):
                num=num/i
                print(i)
        else:
            i=i+1
    exit()

