'''
Created on 26 de mar de 2018

@author: Romulo
'''
from math import fabs, sqrt

def mysqrt(num):
    guess = float(num/2)
    delta = float(num/2)
    while (delta>1e-15):
        finalGuess = (guess + num/guess)/2
        #print(finalGuess)
        delta = fabs(finalGuess - guess)
        guess = finalGuess
    print(float(num) , str(finalGuess).ljust(18), str(sqrt(num)).ljust(18), fabs(finalGuess - sqrt(num)))   
    return None

if __name__ == '__main__':
    print("a    mysqrt(a)         math.sqrt(a)      diff")
    print("---  ----------------  ----------------  -------------------")
    for x in range(10,21):
        mysqrt(x)
