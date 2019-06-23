'''
Created on 26 de mar de 2018

@author: Romulo

'''

def gcd(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    # Your code here
    if(a<=b):
        if(b%a==0):
            return a
        else:
            return gcd(a, b%a)
    if(b<a):
        if(a%b==0):
            return b
        else:
            return gcd(a%b , b)

if __name__ == '__main__':
    print(gcd(32, 16))