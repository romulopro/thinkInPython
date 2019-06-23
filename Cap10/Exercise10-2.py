'''
Created on 15 de mai de 2018

@author: Romulo
'''
def cumsum(lista):
    listOfCumulativeSum = []
    result = 0
    for item in lista:
        result += item
        listOfCumulativeSum.append(result)
    return listOfCumulativeSum
if __name__ == '__main__':
    print(cumsum([1, 2, 3, 7]))