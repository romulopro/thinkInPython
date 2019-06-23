'''
Created on 20 de mar de 2018

@author: Romulo
'''
def isTriangle(sideA, sideB, sideC):
    if (sideA+sideB < sideC or 
        sideB+sideC < sideA or 
        sideC+sideA < sideB):
        print("No")
    else:
        print("Yes")
    return None
    

if __name__ == '__main__':
    sideA = int(input())
    sideB = int(input())
    sideC = int(input())
isTriangle(sideA, sideB, sideC)
    

    
        