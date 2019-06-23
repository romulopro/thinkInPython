# -*- coding: utf-8 -*-
'''
Created on 20 de mar de 2018

@author: Romulo
'''

if __name__ == '__main__':
    a = int(input("Enter 'a' parameter: "))
    b = int(input("Enter 'b' parameter: "))
    c = int(input("Enter 'c' parameter: "))
    n = int(input("Enter 'n' parameter: "))
    
    if(n<=2):
        print("'n' must be greater than 2")
    elif(a**n + b**n == c**n):
        print("Holy somke, Fermat was wrong")
    else:
        print("No, that doesn't work")

    
    