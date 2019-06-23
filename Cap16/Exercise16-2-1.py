'''
Created on 18 de dez de 2018

@author: Romulo
'''
from datetime import datetime

def main():
    day, month, year = map(int, input("Type your birthday in dd mm aaaa format: \n").split())
    actual_date = datetime.now()
    if(actual_date.month > month): 
        year = actual_date.year + 1
    elif(actual_date.month == month and actual_date.day > day ):
        year = actual_date.year + 1
    else:
        year = actual_date.year
    birthday = datetime(year, month, day, 0, 0, 0, 0, tzinfo=None, fold=0)
    if(actual_date.month == month and  actual_date.day == day):
        print("Aniversario eh hoje")
        return None
    time_until_next_birthday = (birthday - actual_date)
    print(" %d dias, %d horas, %d minutos  e %d segundos ate o proximo aniversario" %(time_until_next_birthday.days, time_until_next_birthday.seconds//3600 , (time_until_next_birthday.seconds%3600)//60, (time_until_next_birthday.seconds%3600)%60))
    return None

if __name__ == '__main__':
    main()