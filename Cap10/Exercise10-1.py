'''
Created on 15 de mai de 2018

@author: Romulo
'''
def nested_sum(lista):
    s = 0
    for element in lista:
        if len(element) != 0:
            s += sum(element) 
    return s
if __name__ == '__main__':
    print(nested_sum([[1, 2], [3], [4, 5, 6]]))