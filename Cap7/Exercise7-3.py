'''
Created on 28 de mar de 2018

@author: Romulo
'''
import math
def estimate_pi():
    x = 0
    calculatedPi = 0
    sumTerms = 0
    serieTerm = 1
    factor = 2*math.sqrt(2) / 9801
    while(serieTerm>1e-15):
        serieTerm =  (math.factorial(4*x) * (1103+26930*x))/((math.factorial(x))**4 * 396**(4*x))
        sumTerms += serieTerm 
        x = x+1
    calculatedPi = 1/(factor*sumTerms)
        
    print(calculatedPi)
    return None
if __name__ == '__main__':
    estimate_pi()