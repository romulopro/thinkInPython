'''
Created on 30 de dez de 2018

@author: Romulo
'''
from datetime import date, timedelta

def main():
     dayBirth1, monthBirth1, yearBirth1 = map(int, input("Type your birthday in dd mm aaaa format: \n").split())
     dayBirth2, monthBirth2, yearBirth2 = map(int, input("Type your birthday in dd mm aaaa format: \n").split())
     timesOlder = int(input("How many times older :\n"))
     birthday1 = date(yearBirth1, monthBirth1, dayBirth1)
     birthday2 = date(yearBirth2, monthBirth2, dayBirth2)
     deltaBirthdate = (timesOlder / (timesOlder - 1))*(birthday2 - birthday1)
     #print(deltaBirthdate)
     print(birthday1 + ((deltaBirthdate)))
if __name__ == '__main__':
    main()