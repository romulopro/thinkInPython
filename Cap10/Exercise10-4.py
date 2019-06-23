'''
Created on 16 de mai de 2018

@author: Romulo
'''
def chop(list):
    list.pop()
    list.pop(0)
    return None

if __name__ == '__main__':
    list1 = [1, 3, 9, 7, 7, 4]
    chop(list1)
    print(list1)