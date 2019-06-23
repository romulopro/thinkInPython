'''
Created on 17 de mai de 2018

@author: Romulo
'''
from random import randint

if __name__ == '__main__':
    numOfSameBirthdays = 0
    for _ in range (3200):
        listOfBirthdays = []
        for _ in range(23):
            listOfBirthdays.append(randint(0, 366))
        if len(listOfBirthdays) != len(set(listOfBirthdays)):
            numOfSameBirthdays += 1
    print( "%.3f %%" %(numOfSameBirthdays*100/3200))